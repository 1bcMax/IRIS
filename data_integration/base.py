class DataSource(ABC):
    """Abstract base class for data sources."""
    
    @abstractmethod
    async def connect(self) -> None:
        """Establish connection to the data source."""
        
    @abstractmethod
    async def fetch_data(self, query: Query) -> Iterator[Data]:
        """Fetch data from the source."""