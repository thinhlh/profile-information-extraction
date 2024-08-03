import openai
import os

CHAT_MODEL = os.getenv("CHAT_MODEL")
client = openai.AzureOpenAI(
  api_key=os.getenv("API_KEY"),
  azure_endpoint=os.getenv("ENDPOINT"),
  api_version=os.getenv("API_VERSION"),
  azure_deployment = os.getenv("AZURE_DEPLOYMENT")
)