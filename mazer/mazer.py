import image_generator
import random


def generate_random(size = 100, start=0, end=0):
    points = []

    for i in range(size):
        for x in range(size):
          if bool(random.getrandbits(1)):
              points.append((i, x))

    return points
    #image_generator.generate_photo_with_points('test.png', points, size)

def generate_simple_maze(size = 100, start=(0,0), end=(0,0)):
    if end == (0,0):
        end = (size, size)

    current_cell = start

    for i in range(size):
        direction = random.randint(4)
        

generate_maze(size=10000)
