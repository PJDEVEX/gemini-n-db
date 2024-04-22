import os
from dotenv import load_dotenv
import unittest
from unittest.mock import patch, MagicMock
from src.ai.generator import get_gemini_response

load_dotenv()

MODEL = os.getenv("MODEL")

class TestGenerator(unittest.TestCase):
    @patch('src.ai.generator.GenerativeModel')
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


    @patch('src.ai.generator.GenerativeModel')
    def test_get_gemini_response_failure_loading_model(self, mock_generative_model):
        """
        Test the get_gemini_response function for failure in loading the model
        """
        # Mocking the GenerativeModel class to raise ImportError
        mock_generative_model.side_effect = ImportError("Failed to load the model")
        
        # Call the function with sample parameters and assert for RuntimeError
        with self.assertRaises(RuntimeError):
            get_gemini_response("Sample question", "Sample prompt")
    
    @patch('src.ai.generator.GenerativeModel')
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