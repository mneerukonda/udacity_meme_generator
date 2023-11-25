"""A abstract base class for Ingestors.

This is a abstract base class which is extended by multiple ingestor child classes,
the method provided here are used to check if a file can be ingested based on the expected extensions
and a abstract method parse which will be implemented by all the sub classes to parse that
particular file.
"""
from abc import ABC, abstractmethod
from typing import List

from QuoteEngine.quote import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for all the Ingestor classes.

    IngestorInterface is used by mutiple base classes which implement the parse method
    to parse different types of files and return a QuoteModel objects.
    """

    expected_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Check for Ingested file type.

        If the file extension is in one of the expected extensions then this method return true else false.
        """
        ext = path.split('.')[-1]
        if ext in cls.expected_extensions:
            return True
        else:
            return False

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse different file types.

        This abstract method will be implemented by the child classes to parse different kinds of file types.
        """
        pass
