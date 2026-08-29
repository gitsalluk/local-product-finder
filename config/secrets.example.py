# DO NOT COMMIT THIS FILE WITH REAL SECRETS!
# Copy this to config/secrets.py and fill in your actual values.
# config/secrets.py is listed in .gitignore and will never be committed.

import os
from dotenv import load_dotenv

# Load from .env file if it exists (for local development)
load_dotenv()

# Example API Keys and Credentials
# Replace these with your actual values or set as environment variables

AMAZON_API_KEY = os.getenv('AMAZON_API_KEY', 'your-amazon-api-key-here')
AMAZON_API_SECRET = os.getenv('AMAZON_API_SECRET', 'your-amazon-secret-here')

TARGET_API_KEY = os.getenv('TARGET_API_KEY', 'your-target-api-key-here')

EBAY_API_KEY = os.getenv('EBAY_API_KEY', 'your-ebay-api-key-here')

# User agent for web scraping (to avoid being blocked)
SCRAPY_USER_AGENT = os.getenv(
    'SCRAPY_USER_AGENT',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
)

# Database credentials (if using)
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///products.db')

# Logging level
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

print("⚠️  Using example secrets. Copy this file to config/secrets.py and add real values.")
