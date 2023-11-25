"""This module is to handle csv quote files.

CSVIngestor is part of the strategy pattern to handle the csv files.
The method provided check if the file can be ingested based on the extension
and then reads the csv file and return the content of the csv file as a list
of QuoteModel's.
"""
from typing import List

import pandas as pd

from QuoteEngine.ingestor_interface import IngestorInterface
from QuoteEngine.quote import QuoteModel


class CSVIngestor(IngestorInterface):
    """A subclass of IngestorInterface.

    The CSVIngestor class handles the csv quote files. The purpose of this class
    is to read the quotes in the csv file and then generate the list of QuoteModel's.
    """

    expected_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a csv file.

        Parses the csv file and read the contents of the csv file,
        reads the columns body and author and generate a QuoteModel instance for each
        row in the file and return the list of QuoteModel's.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest csv file')
        quotes = []
        df = pd.read_csv(path, header=0)
        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)
        return quotes
