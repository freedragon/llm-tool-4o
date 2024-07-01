import os

from dotenv import load_dotenv
from pathlib import Path
from promptflow.tracing import trace
from promptflow.core import Prompty

BASE_DIR = Path(__file__).absolute().parent
# print(BASE_DIR)

@trace
def chat(question: str = "What's the capital of France?") -> str:
    """Flow entry function."""

    if "OPENAI_API_KEY" not in os.environ and "AZURE_OPENAI_API_KEY" not in os.environ:
        # load environment variables from .env file
        load_dotenv()

    # Load prompty with dict override
    override_model = {
        "configuration": {
            "api_key": "${env:AZURE_OPENAI_API_KEY}",
            "api_version": "${env:AZURE_OPENAI_API_VERSION}",
            "azure_endpoint": "${env:AZURE_OPENAI_ENDPOINT}"
        },
        "parameters": {"max_tokens": 512}
    }
    prompty = Prompty.load(source=BASE_DIR / "chat.prompty", model=override_model)
    # prompty = Prompty.load(source=BASE_DIR / "chat.prompty")

    # trigger a llm call with the prompty obj
    output = prompty(question=question)
    return output