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


def get_service_account_credentials_and_refresh(key_file) -> Credentials:
    """
    Get the service account credentials & refresh
    """
    try:
        credentials = Credentials.from_service_account_file(
            key_file,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        credentials.refresh(Request())
        print("Credentials loaded successfully!")
        return credentials
    except Exception as e:
        # TODO: Add api error logging (f"Internal Server Error and return 500")
        print(f"get service account credentials error: {e}")
        raise RuntimeError("Failed to load service acccount credentials") from e

# Call get_service_account_credentials_and_refresh
key_file = GOOGLE_APPLICATION_CREDENTIALS
credentials = get_service_account_credentials_and_refresh(key_file)

def initialize_vertexai_client(project_id: str, region: str, credentials: Credentials):
    """
    Initialize the Vertex AI client
    """
    try:
        client = vertexai.init(project=PROJECT_ID)
        print("Vertex AI client initialized successfully!")
        return client
    except Exception as e:
        raise RuntimeError("Failed to initialize Vertex AI client") from e
    
vertexai_client = initialize_vertexai_client(PROJECT_ID, REGION, credentials)