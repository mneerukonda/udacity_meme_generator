"""This module is to handle pdf quote files.

PdfIngestor is part of the strategy pattern to handle the pdf files.
The method provided check if the file can be ingested based on the extension
and then reads the pdf file save the content of the pdf file as a text file and then
read the text file and return the content of the text file as a list
of QuoteModel's.
"""
import os
import random
import subprocess
from typing import List

from QuoteEngine.ingestor_interface import IngestorInterface
from QuoteEngine.quote import QuoteModel
from QuoteEngine.text_parser import TextParser


class PdfIngestor(IngestorInterface):
    """A subclass of IngestorInterface.

    The PdfIngestor class handles the pdf quote files. The purpose of this class
    is to read the quotes in the pdf file and then generate the list of QuoteModel's.
    """

    expected_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a pdf file.

        Parses the pdf file and read the contents of the pdf file,
        reads the pdf file and generate a text file from the content of the pdf file.
        Save the text file in a temp location and then read the text file and split
        each line of the text file into body and author and generate a QuoteModel instance for each
        line in the file and return the list of QuoteModel's.
        In the end remove the temporary txt file.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Pdf file')

        tmp = f'./tmp/{random.randint(0, 1000000)}.txt'
        subprocess.call(['pdftotext', path, tmp])

        with open(tmp, 'r') as file_ref:
            quotes = []
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    quotes.append(TextParser.parse_text(line))
        os.remove(tmp)
        return quotes
