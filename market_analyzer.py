import logging
from typing import Dict, Any
from datetime import datetime, timedelta

class MarketAnalyzer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.data_cache: Dict[str, Any] = {}
        self.cache_expiry: int = 60 * 15  # 15 minutes in seconds
        
    def fetch_market_data(self, source: str) -> Dict[str, Any]:
        """
        Fetches market data from specified sources.
        
        Args:
            source: Data source identifier (e.g., '-news', 'finance_api')
            
        Returns:
            Market data as a dictionary
            
        Raises:
            ConnectionError: If unable to fetch data
            ValueError: If invalid source is provided
        """
        try:
            if source == 'news':
                # Simulated news fetching
                data = {'trend': 'up', 'sentiment': 'positive'}
            elif source == 'finance_api':
                # Simulated finance API call
                data = {'price': 100.5, 'volume': 5000}
            else:
                raise ValueError("Invalid data source")
            
            self._cache_data(source, data)
            return data
            
        except Exception as e:
            self.logger.error(f"Failed to fetch market data from {source}: {str(e)}")
            raise
    
    def _cache_data(self, key: str, data: Dict[str, Any]) -> None:
        """
        Caches market data with expiration.
        
        Args:
            key: Cache key
            data: Data to cache
        """
        self.data_cache[key] = {
            'data': data,
            'expires_at': datetime.now().timestamp() + self.cache_expiry
        }
    
    def get_cached_data(self, key: str) -> Dict[str, Any]:
        """
        Retrieves cached market data if not expired.
        
        Args:
            key: Cache key
            
        Returns:
            Data if available and not expired; None otherwise
        """
        now = datetime.now().timestamp()
        if key in self.data_cache:
            if now < self.data_cache[key]['expires_at']:
                return self.data_cache[key]['data']
            else:
                self.logger.info(f"Cache expired for key: {key}")
                del self.data_cache[key]
        return None