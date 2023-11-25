### Meme Generator

This application generate memes using images and quotes.  
The application picks an image either from the existing image from project or with the image supplied by the user and will create a meme using the quotes supplied by the user or from existing quotes in the project.

### Setup
1. Download the project from git
2. Install python and pip
3. Install the required dependencies from requirements.txt file
4. Install additional required libraries (mentioned the below section)
5. Once everything is set, we can use

      a. To run in cli mode, run `python3 meme.py`   
      b. To run it as a flask application check the flask section below.


### modules
1. QuoteEngine
   1. This module contains the necessary strategy files for loading the quotes from different file types (eg. pdf, csv, docx etc).
2. MemeGenerator
   1. This module create the meme using the supplied image, quote and author.

#### Additional required libraries
- xpdf (apt-get install xpdf)

#### To run a flask application  
export FLASK_APP=app.py   
flask run --host=0.0.0.0 --port=3000

https://images.ctfassets.net/2y9b3o528xhq/4swf2qhcelEUWzKHaKne6C/d890de3220ea332fb42e9b8e5f7848fd/real-world-projects.png