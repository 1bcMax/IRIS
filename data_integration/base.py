from abc import ABC, abstractmethod

class DataSource(ABC):
    """Abstract base class for data sources."""
    
    @abstractmethod
    async def connect(self):
        """Establish connection to the data source."""
        pass
        
    @abstractmethod
    async def fetch_data(self, query):
        """Fetch data from the source."""
        pass
