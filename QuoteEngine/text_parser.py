"""For parsing a input into QuoteModel.

This class has a static method to parse a given line into a QuoteModel
by splitting the content of the input text and cleaning it up.
"""
from QuoteEngine.quote import QuoteModel


class TextParser():
    """A Text Parser.

    Parses the input to generate a QuoteModel object.
    """

    @staticmethod
    def parse_text(input):
        """Parse the input text.

        Split the text on '-' and generate the QuoteModel with body and author.
        """
        row = input.split('-')
        quote = QuoteModel(row[0].replace('"', '').strip(), row[1].strip())
        return quote
