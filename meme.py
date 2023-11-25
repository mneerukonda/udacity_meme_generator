"""Generate a Meme from cli.

The generate_meme function generates a meme based on the path provided as input or from a random existing image,
and body and author provided a input in cli or by selecting a random text from the existing quotes, and then return the
path of the generated meme image.
"""
import argparse
import os
import random

from MemeGenerator.meme_generator import MemeEngine
from QuoteEngine.ingestor import Ingestor
from QuoteEngine.quote import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    praser = argparse.ArgumentParser(description='Argument parser for meme generator')

    praser.add_argument('--path', type=str)
    praser.add_argument('--body', type=str)
    praser.add_argument('--author', type=str)

    args = praser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
