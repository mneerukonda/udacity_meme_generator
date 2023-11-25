"""Application used by Flask.

The setup function is used to load all the existing quotes and images list and return them
so that a random image and quote can be selected to genereate a meme

The meme_random is called when the flask application is loaded or when random button is clicked on screen.
The meme_form is called when the user wants to enter the details of the image text and author.
The meme_post is called to save the image, text and author the user has entered to create a new meme.
"""
import os
import random

import requests
from flask import Flask, render_template, request

from MemeGenerator.meme_generator import MemeEngine
from QuoteEngine.ingestor import Ingestor
from QuoteEngine.quote import QuoteModel

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []

    for q_file in quote_files:
        quotes.extend(Ingestor.parse(q_file))

    images_path = "_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs.extend([os.path.join(root, name) for name in files])

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get('image_url')
    file_name = image_url.split('/')[-1]
    out_file = f'./tmp/{file_name}'

    resp = requests.get(image_url)

    with open(out_file, 'wb') as image_file:
        image_file.write(resp.content)

    quote = QuoteModel(request.form.get('body'), request.form.get('author'))
    path = meme.make_meme(out_file, quote.body, quote.author)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
