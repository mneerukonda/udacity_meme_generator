"""Represent model for Quotes.

The QuoteModel represent a quote and its author.
"""


class QuoteModel:
    """A quote model.

    A QuoteModel encapsulates the body and author of a quote.
    """

    def __init__(self, body, author):
        """Initialize the quote body and author."""
        self.body = body
        self.author = author

    def __str__(self):
        """Return `str(self)`, a human-readable string representation of this object."""
        return f'{self.body} by {self.author}'

    def __repr__(self):
        """Return `repr(self)`, a human-readable string representation of this object."""
        return f'{self.body} by {self.author}'
