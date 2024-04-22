import os
import unittest
from dotenv import load_dotenv
from unittest.mock import patch, MagicMock
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from src.gcp.gcp_confi import (
    get_service_account_credentials_and_refresh,
    initialize_vertexai_client,
    get_gemini_response,
)


# Load the environment variables
load_dotenv()

# Define the env var
GOOGLE_APPLICATION_CREDENTIALS = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS"
)
MODEL = os.getenv("MODEL")
PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION")



class TestApp(unittest.TestCase):
    @patch('src.gcp.gcp_confi.Credentials')
    @patch('src.gcp.gcp_confi.Request')
    def test_get_service_account_credentials_and_refresh_success(self, mock_request, mock_credentials):
        """
        Test the get_service_account_credentials_and_refresh function
        """
        # Mocking
        mock_credentials.from_service_account_file.return_value = mock_credentials
        mock_credentials.refresh.return_value = None

        credentials = get_service_account_credentials_and_refresh(GOOGLE_APPLICATION_CREDENTIALS)
        
        # Asserting
        self.assertIsNotNone(credentials)
        mock_credentials.from_service_account_file.assert_called_once_with(
            GOOGLE_APPLICATION_CREDENTIALS,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        mock_credentials.refresh.assert_called_once_with(mock_request())

    def test_get_service_account_credentials_and_refresh_failure(self):
        """
        Test the get_service_account_credentials_and_refresh function
        """
        with self.assertRaises(RuntimeError):
            get_service_account_credentials_and_refresh("non_existing_key_file.json")
    
    def test_initialize_vertexai_client_success(self):
        """
        Test the initialize_vertexai_client function
        """
        with patch('src.gcp.gcp_confi.vertexai.init') as mock_init:
            # mocking
            mock_client = MagicMock()
            mock_init.return_value = mock_client

            # calling the function
            client = initialize_vertexai_client(PROJECT_ID, REGION, Credentials)

            # asserting
            self.assertEqual(client, mock_client)
            mock_init.assert_called_once_with(project=PROJECT_ID)
    
    def test_initialize_vertexai_client_failure(self):
        """
        Test the initialize_vertexai_client function
        """
        with patch('src.gcp.gcp_confi.vertexai.init') as mock_init:
            # mocking
            mock_init.side_effect = Exception("Failed to initialize Vertex AI client")

            # calling the function
            with self.assertRaises(RuntimeError):
                initialize_vertexai_client(PROJECT_ID, REGION, Credentials)
    

    @patch('src.gcp.gcp_confi.GenerativeModel')
    def test_get_gemini_response_success(self, mock_generative_model):
        """
        Test the get_gemini_response function for success
        """
        # Mocking the GenerativeModel instance and its generate_content method
        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.return_value.text = "Generated response"
        mock_generative_model.return_value = mock_model_instance
        
        # Call the function with sample parameters
        response = get_gemini_response("Sample question", "Sample prompt")
        
        # Assertions
        self.assertEqual(response, "Generated response")
        mock_generative_model.assert_called_once_with(MODEL)
        mock_model_instance.generate_content.assert_called_once_with(["Sample question", "Sample prompt"])


    @patch('src.gcp.gcp_confi.GenerativeModel')
    def test_get_gemini_response_failure_loading_model(self, mock_generative_model):
        """
        Test the get_gemini_response function for failure in loading the model
        """
        # Mocking the GenerativeModel class to raise ImportError
        mock_generative_model.side_effect = ImportError("Failed to load the model")
        
        # Call the function with sample parameters and assert for RuntimeError
        with self.assertRaises(RuntimeError):
            get_gemini_response("Sample question", "Sample prompt")
    
    @patch('src.gcp.gcp_confi.GenerativeModel')
    def test_get_gemini_response_failure_generating_content(self, mock_generative_model):
        """
        Test the get_gemini_response function for failure in generating content
        """
        # Mocking the GenerativeModel instance and its generate_content method to raise an exception
        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.side_effect = Exception("Failed to generate content")
        mock_generative_model.return_value = mock_model_instance
        
        # Call the function with sample parameters and assert for RuntimeError
        with self.assertRaises(RuntimeError):
            get_gemini_response("Sample question", "Sample prompt")

if __name__ == '__main__':
    unittest.main()
