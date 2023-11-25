"""This module handles all the Ingestors.

The Ingestor class encapsulates all the ingestors to provide
one interface to load any supported file type.
"""
from typing import List

from QuoteEngine.csv_ingestor import CSVIngestor
from QuoteEngine.docx_ingestor import DocxIngestor
from QuoteEngine.ingestor_interface import IngestorInterface
from QuoteEngine.pdf_ingestor import PdfIngestor
from QuoteEngine.quote import QuoteModel
from QuoteEngine.text_ingestor import TextIngestor


class Ingestor(IngestorInterface):
    """Encapsulates all the Ingestors.

    The Ingestor class based on the input decides which ingestor's
    parse method should be called based on the extension of the input file
    """

    ingestors = [DocxIngestor, CSVIngestor, PdfIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select a parser.

        Loop through the list of ingestors and then select one ingestor based on the
        the extension of the file type and call it's parse method to get the list
        of QuoteModel.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
