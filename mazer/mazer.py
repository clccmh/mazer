import image_generator
from PIL import Image
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

    wall_list = []
    passage_walls = []
    part_of_maze = []

    # Pick a cell, mark it as part of the maze
    part_of_maze.append(start)

    #Add the walls of the cell to the wall list
    for i in range(4):
        wall_list.append((start + (i,)))

    while len(wall_list):
        # Pick a random wall
        wall = wall_list[random.randint(0, len(wall_list)-1)]

        # Check if there is one unvisited cell
        if wall[2] == 0:
            if wall[0]+1 >= 0 and wall[0]+1 < size and (wall[0]+1, wall[1]) not in part_of_maze:
                passage_walls.append(wall)
                new_cell = (wall[0]+1, wall[1])
                part_of_maze.append(new_cell)
                for i in [0,2,3]:
                    wall_list.append((new_cell + (i,)))

        elif wall[2] == 1:
            if wall[0]-1 >= 0 and wall[0]-1 < size and (wall[0]-1, wall[1]) not in part_of_maze:
                passage_walls.append(wall)
                new_cell = (wall[0]-1, wall[1])
                part_of_maze.append(new_cell)
                for i in [1, 2, 3]:
                    wall_list.append((new_cell + (i,)))
                
        elif wall[2] == 2:
            if wall[1]+1 >= 0 and wall[1]+1 < size and (wall[0], wall[1]+1) not in part_of_maze:
                passage_walls.append(wall)
                new_cell = (wall[0], wall[1]+1)
                part_of_maze.append(new_cell)
                for i in [0, 1, 2]:
                    wall_list.append((new_cell + (i,)))
                
        
        elif wall[2] == 3:
            if wall[1]-1 >= 0 and wall[1]-1 < size and (wall[0], wall[1]-1) not in part_of_maze:
                passage_walls.append(wall)
                new_cell = (wall[0], wall[1]-1)
                part_of_maze.append(new_cell)
                for i in [0, 1, 3]:
                    wall_list.append((new_cell + (i,)))

        wall_list.remove(wall)

        # If there is
            # Make the wall a passage
            # Mark the unvisited cell as part of the maze
            # Add that cell's walls to the wall list
        # Remove the wall from the list
    return [part_of_maze, passage_walls]


maze = generate_simple_maze()
im = image_generator.generate_new_photo(100)
image_generator.add_cells_to_maze(im, maze[0])
image_generator.add_passages_to_maze(im, maze[1])
image_generator.save_photo(im, 'test.png')
