from abc import ABC, abstractmethod

class InsightGenerator(ABC):
    """Abstract base class for insight generators."""
    
    @abstractmethod
    async def generate_insights(self, patterns):
        """Generate insights from patterns."""
        pass
        
    @abstractmethod
    async def rank_insights(self, insights):
        """Rank insights by relevance."""
        pass
