import image_generator
import random

def generate_maze(size = 100, start=0, end = size):
    points = []
    visited = []
    current_point = (0, 0)
    while current_point != (end, end) and has_sides():
        
        

    image_generator.generate_photo_with_points('test.png', points, size)

generate_maze(size=5000)
