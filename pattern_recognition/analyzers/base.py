class PatternAnalyzer(ABC):
    """Abstract base class for pattern analyzers."""
    
    @abstractmethod
    async def analyze(self, data: Data) -> List[Pattern]:
        """Analyze data for patterns."""
        
    @abstractmethod
    async def validate_pattern(self, pattern: Pattern) -> bool:
        """Validate identified pattern."""