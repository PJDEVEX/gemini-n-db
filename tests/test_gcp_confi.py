import os
import unittest
from dotenv import load_dotenv
from unittest.mock import patch
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from src.gcp.gcp_confi import get_service_account_credentials_and_refresh


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


if __name__ == '__main__':
    unittest.main()
