"""Command-line interface for Local Product Finder."""

import sys
from config.settings import SUPPORTED_COUNTRIES, PRODUCT_CATEGORIES
from src.scrapers.demo_scraper import DemoScraper
from src.utils.logger import get_logger

logger = get_logger(__name__)

class CLI:
    """Command-line interface for user interaction."""
    
    def __init__(self):
        self.scraper = None
    
    def display_welcome(self):
        """Display welcome message."""
        print("\n" + "="*60)
        print("  🔍 LOCAL PRODUCT FINDER")
        print("  Find local products by type across different countries")
        print("="*60 + "\n")
    
    def get_country(self) -> str:
        """Prompt user to select a country."""
        print("Available countries:")
        for code, info in SUPPORTED_COUNTRIES.items():
            print(f"  {code}: {info['name']}")
        
        while True:
            country = input("\nEnter country code (e.g., US, UK, CA): ").upper().strip()
            if country in SUPPORTED_COUNTRIES:
                logger.info(f"Selected country: {SUPPORTED_COUNTRIES[country]['name']}")
                return country
            print(f"❌ '{country}' not recognized. Please try again.")
    
    def get_product_query(self) -> str:
        """Prompt user for product search query."""
        print("\nWhat product are you looking for?")
        print("Examples: clarifying shampoo, vitamin D, face mask, etc.")
        query = input("\nEnter product name or type: ").strip()
        
        if not query:
            print("❌ Please enter a valid product name.")
            return self.get_product_query()
        
        logger.info(f"Searching for: {query}")
        return query
    
    def display_results(self, products):
        """Display search results to user."""
        if not products:
            print("\n❌ No products found.")
            return
        
        print(f"\n✅ Found {len(products)} products:\n")
        print("-" * 80)
        
        for i, product in enumerate(products, 1):
            print(f"\n{i}. {product.name}")
            print(f"   Retailer: {product.retailer}")
            print(f"   Price: {product.currency} {product.price}")
            if product.rating:
                print(f"   Rating: {'⭐' * int(product.rating)} ({product.rating}/5)")
            print(f"   Status: {'✅ In Stock' if product.in_stock else '❌ Out of Stock'}")
            print(f"   Description: {product.description}")
            print(f"   URL: {product.url}")
        
        print("\n" + "-" * 80)
    
    def run(self):
        """Run the CLI application."""
        self.display_welcome()
        
        try:
            # Get user input
            country = self.get_country()
            query = self.get_product_query()
            
            # Search for products
            print("\n🔄 Searching...\n")
            self.scraper = DemoScraper(country=country)
            products = self.scraper.search(query)
            
            # Display results
            self.display_results(products)
            
            # Ask if user wants to search again
            again = input("\nSearch again? (y/n): ").lower().strip()
            if again == 'y':
                self.run()
            else:
                print("\n👋 Thank you for using Local Product Finder!\n")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Application interrupted.")
            logger.info("User interrupted the application")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            logger.error(f"Unexpected error: {e}", exc_info=True)
        finally:
            if self.scraper:
                self.scraper.close()
