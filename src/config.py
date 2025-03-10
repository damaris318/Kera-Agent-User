import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database Config
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DATABASE")

DATABASE_SCHEMA = os.getenv("DATABASE_SCHEMA")

# Azure API Config
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION")