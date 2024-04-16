import os
from dotenv import load_dotenv
import vertexai
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from vertexai.generative_models import GenerativeModel, Part


# Load the environment variables
load_dotenv()

# Define the env var
GOOGLE_APPLICATION_CREDENTIALS = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS"
)
MODEL = os.getenv("MODEL")
PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION")


def get_service_account_credentials_and_refresh() -> Credentials:
    """
    Get the service account credentials
    """
    try:
        credentials = Credentials.from_service_account_file(
            GOOGLE_APPLICATION_CREDENTIALS,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        credentials.refresh(Request())
        print("Credentials loaded successfully!")
        return credentials
    except Exception as e:
        # TODO: Add api error logging (f"Internal Server Error and return 500")
        print(f"get service account credentials error: {e}")
        return None, False
