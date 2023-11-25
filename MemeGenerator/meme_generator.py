"""Generate a meme image.

This module is used for generating a meme image using the Pillow module.
"""
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """An Engine to generate a meme image.

    The purpose of this class is to generate a meme based on the input image, text and author.
    The meme text and author are imposed on the file and the outfile is saved in a temp location
    specified while creating a MemeEngine object.
    """

    def __init__(self, out_path):
        """Create a new MemeEngine.

        @param out_path: The location where the finished meme file should be stored.
        """
        self.out_path = out_path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make a meme.

        This method takes the input image, resizes the image and then draws the text and the author
        on the image using the font that is mentioned in this method and then saves the file in
        the location specified while creating the MemeEngine.
        """
        img = Image.open(img_path)

        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        message = text + ' - ' + author
        if message is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((10, 30), message, font=font, fill='white')
        file_name = img_path.split('/')[-1]
        file_path = f'{self.out_path}/{file_name}'
        img.save(file_path)
        return file_path
