# Application Settings

# Supported countries for product search
SUPPORTED_COUNTRIES = {
    'US': {'name': 'United States', 'language': 'en', 'currency': 'USD'},
    'UK': {'name': 'United Kingdom', 'language': 'en', 'currency': 'GBP'},
    'CA': {'name': 'Canada', 'language': 'en', 'currency': 'CAD'},
    'DE': {'name': 'Germany', 'language': 'de', 'currency': 'EUR'},
    'FR': {'name': 'France', 'language': 'fr', 'currency': 'EUR'},
    'JP': {'name': 'Japan', 'language': 'ja', 'currency': 'JPY'},
}

# Product categories
PRODUCT_CATEGORIES = [
    'Hair Care',
    'Skincare',
    'Personal Care',
    'Beauty',
    'Makeup',
    'Fragrance',
    'Supplements',
    'Wellness',
]

# Scraping settings
SCRAPE_TIMEOUT = 10  # seconds
MAX_RETRIES = 3
CACHE_DURATION = 3600  # seconds (1 hour)

# Data storage
CACHE_DIR = 'data/cache'
OUTPUT_DIR = 'data/output'
