from typing import List
from src.scrapers.base_scraper import BaseScraper
from src.models.product import Product
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DemoScraper(BaseScraper):
    """Demo scraper that returns sample products without actual web scraping.
    
    This is a placeholder while you build real scrapers.
    Replace this with actual BeautifulSoup/requests scraping.
    """
    
    def search(self, query: str) -> List[Product]:
        """Return demo products matching the query."""
        logger.info(f"Demo search for '{query}' in {self.country}")
        
        # Sample data - replace with real scraping
        demo_products = [
            Product(
                name="Premium Clarifying Shampoo",
                description="Deep cleansing shampoo that removes buildup and residue",
                price=12.99,
                currency="USD" if self.country == "US" else "GBP",
                country=self.country,
                retailer="Demo Store",
                url="https://example.com/product1",
                category="Hair Care",
                rating=4.5,
                in_stock=True
            ),
            Product(
                name="Organic Clarifying Shampoo",
                description="Natural ingredients, sulfate-free clarifying shampoo",
                price=15.99,
                currency="USD" if self.country == "US" else "GBP",
                country=self.country,
                retailer="Demo Store",
                url="https://example.com/product2",
                category="Hair Care",
                rating=4.8,
                in_stock=True
            ),
            Product(
                name="Clarifying Treatment Mask",
                description="Weekly clarifying mask for scalp and hair",
                price=18.99,
                currency="USD" if self.country == "US" else "GBP",
                country=self.country,
                retailer="Demo Store",
                url="https://example.com/product3",
                category="Hair Care",
                rating=4.3,
                in_stock=True
            ),
        ]
        
        logger.info(f"Found {len(demo_products)} demo products")
        return demo_products
