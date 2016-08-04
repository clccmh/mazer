
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor

CELL_SIZE = 10

def generate_new_photo(size):
    return Image.new('RGB', [(size*2+1)*CELL_SIZE, (size*2+1)*CELL_SIZE], color='black')


def add_cells_to_maze(photo, points):
    im = photo

    draw = ImageDraw.Draw(im, mode='RGB')

    for point in points:
        draw.point((point[0]*2 + 1, point[1]*2 + 1), fill='white')
    del draw

    return im

def add_passages_to_maze(photo, points):
    im = photo

    draw = ImageDraw.Draw(im, mode='RGB')

    for point in points:
        if point[2] == 0:
            draw.point((point[0]*2 + 2, point[1]*2 + 1), fill='white')
        elif point[2] == 1:
            draw.point((point[0]*2 - 0, point[1]*2 + 1), fill='white')
        elif point[2] == 2:
            draw.point((point[0]*2 + 1, point[1]*2 + 2), fill='white')
        elif point[2] == 3:
            draw.point((point[0]*2 + 1, point[1]*2 - 0), fill='white')
    del draw

    return im


def save_photo(photo, name):
    photo.save(name)
