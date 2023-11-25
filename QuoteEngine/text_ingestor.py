"""This module is to handle txt quote files.

TextIngestor is part of the strategy pattern to handle the txt files.
The method provided check if the file can be ingested based on the extension
and then reads the text file and return the content of the text file as a list
of QuoteModel's.
"""
from typing import List

from QuoteEngine.ingestor_interface import IngestorInterface
from QuoteEngine.quote import QuoteModel
from QuoteEngine.text_parser import TextParser


class TextIngestor(IngestorInterface):
    """A subclass of IngestorInterface.

    The TextIngestor class handles the text quote files. The purpose of this class
    is to read the quotes in the txt file and then generate the list of QuoteModel's.
    """

    expected_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a csv file.

        Parses the csv file and read the contents of the csv file,
        reads the columns body and author and generate a QuoteModel instance for each
        row in the file and return the list of QuoteModel's.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest txt file')
        quotes = []
        with open(path, 'r') as file_ref:
            for line in file_ref.readlines():
                if len(line) > 0:
                    quotes.append(TextParser.parse_text(line))
        return quotes
