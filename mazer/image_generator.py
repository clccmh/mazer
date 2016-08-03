
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor


def generate_photo(name, lines, size):

    im = Image.new('RGB', [size, size], color='white')

    draw = ImageDraw.Draw(im, mode='RGB')

    for line in lines:
        draw.line(line, fill=0)
    #draw.line((0, im.size[1], im.size[0], 0), fill=0)
    del draw

    im.save(name)
