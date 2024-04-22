
import os
from dotenv import load_dotenv
from vertexai.generative_models import GenerativeModel, Part

# Load the environment variables
load_dotenv()

# Define the env var
MODEL = os.getenv("MODEL")

def get_gemini_response(question, prompt):
    """
    This function is used to generate content using the generative model.

    Parameters:
    question (str): The question to be answered.
    prompt (str): The prompt for the model.

    Returns:
    str: The generated content.
    """
    try:
        model =GenerativeModel(MODEL)
    except ImportError as e:
        print(f"Error: {e}")
        raise RuntimeError("Failed to load the model") from e
    try:
        response = model.generate_content([question, prompt])
    except Exception as e:
        print(f"Error: {e}")
        raise RuntimeError("Failed to generate content") from e
    return response.text

