from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class Product:
    """Represents a product found during scraping."""
    name: str
    description: str
    price: float
    currency: str
    country: str
    retailer: str
    url: str
    category: str = "Unknown"
    image_url: Optional[str] = None
    rating: Optional[float] = None
    in_stock: bool = True
    scraped_at: datetime = field(default_factory=datetime.now)
    
    def __str__(self):
        return f"{self.name} (${self.price} {self.currency}) from {self.retailer}"
    
    def to_dict(self):
        """Convert product to dictionary."""
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'currency': self.currency,
            'country': self.country,
            'retailer': self.retailer,
            'url': self.url,
            'category': self.category,
            'image_url': self.image_url,
            'rating': self.rating,
            'in_stock': self.in_stock,
            'scraped_at': self.scraped_at.isoformat(),
        }
