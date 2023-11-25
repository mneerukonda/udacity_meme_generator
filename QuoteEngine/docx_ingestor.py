"""This module is to handle docx quote files.

DocxIngestor is part of the strategy pattern to handle the docx files.
The method provided check if the file can be ingested based on the extension
and then reads the docx file and return the content of the docx file as a list
of QuoteModel's.
"""
from typing import List

import docx

from QuoteEngine.ingestor_interface import IngestorInterface
from QuoteEngine.quote import QuoteModel
from QuoteEngine.text_parser import TextParser


class DocxIngestor(IngestorInterface):
    """A subclass of IngestorInterface.

    The DocxIngestor class handles the docx quote files. The purpose of this class
    is to read the quotes in the docx file and then generate the list of QuoteModel's.
    """

    expected_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a docx file.

        Parses the docx file and read the contents of the docx file
        reads the data and split the text into body and author and generate a QuoteModel instance for each
        line in the file and return the list of QuoteModel's.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest docx file')
        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != '':
                quotes.append(TextParser.parse_text(para.text))
        return quotes
