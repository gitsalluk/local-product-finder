from abc import ABC, abstractmethod
from typing import List, Optional
import requests
from src.models.product import Product
from src.utils.logger import get_logger

logger = get_logger(__name__)

class BaseScraper(ABC):
    """Abstract base class for all product scrapers."""
    
    def __init__(self, country: str, user_agent: str = None):
        self.country = country
        self.user_agent = user_agent or 'ProductFinder/1.0'
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': self.user_agent})
    
    @abstractmethod
    def search(self, query: str) -> List[Product]:
        """Search for products matching the query.
        
        Args:
            query: Product name or description to search for
            
        Returns:
            List of Product objects found
        """
        pass
    
    def _fetch_url(self, url: str, timeout: int = 10) -> Optional[str]:
        """Safely fetch a URL and return HTML content.
        
        Args:
            url: URL to fetch
            timeout: Request timeout in seconds
            
        Returns:
            HTML content or None if request fails
        """
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
    
    def close(self):
        """Close the session."""
        self.session.close()
