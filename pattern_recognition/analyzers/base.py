from abc import ABC, abstractmethod

class PatternAnalyzer(ABC):
    """Abstract base class for pattern analyzers."""
    
    @abstractmethod
    async def analyze(self, data):
        """Analyze data for patterns."""
        pass
        
    @abstractmethod
    async def validate_pattern(self, pattern):
        """Validate identified pattern."""
        pass
