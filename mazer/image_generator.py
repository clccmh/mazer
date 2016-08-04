
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor

def generate_new_photo(size):
    return Image.new('RGB', [size*2, size*2], color='black')


def add_cells_to_maze(photo, points):
    im = photo

    draw = ImageDraw.Draw(im, mode='RGB')

    for point in points:
        draw.point((point[0]*2, point[1]*2), fill=0)
    del draw

    return im

def add_passages_to_maze(photo, points):
    im = photo

    draw = ImageDraw.Draw(im, mode='RGB')

    for point in points:
        if point[2] == 0:
            draw.point((point[0]*2 + 1, point[1]*2), fill=0)
        elif point[2] == 1:
            draw.point((point[0]*2 - 1, point[1]*2), fill=0)
        elif point[2] == 2:
            draw.point((point[0]*2, point[1]*2 + 1), fill=0)
        elif point[2] == 3:
            draw.point((point[0]*2, point[1]*2 - 1), fill=0)
    del draw

    return im


def save_photo(photo, name):
    photo.save(name)
