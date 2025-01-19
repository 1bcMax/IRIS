class InsightGenerator(ABC):
    """Abstract base class for insight generators."""
    
    @abstractmethod
    async def generate_insights(self, patterns: List[Pattern]) -> List[Insight]:
        """Generate insights from patterns."""
        
    @abstractmethod
    async def rank_insights(self, insights: List[Insight]) -> List[Insight]:
        """Rank insights by relevance."""