
import pygame
from pygame import Rect

class Block:

    # static variable keeps track of the width of each block; is set through the maze_solver class
    block_width = -1

    # static variable keeps track of the width of the walls between blocks
    wall_width = -1

    def __init__(self, x, y, isWall):
        # storing the x-coordinate of the top-left corner of the Block
        self.x = x

        # storing the y-coordinate of the top-left corner of the Block
        self.y = y

        # storing a boolean value that maintains whether 
        self.isWall = isWall

    def draw(self, Window, specificColor=None):
        # if the current Block is a wall, then the color variable is set to gray as that is the color it should be colored with
        if self.isWall:
            # setting the color to a tuple that corresponds to the color gray
            color = (128, 128, 128)
        else:
            # setting the color to a tuple that corresponds to the color white 
            color = (255, 255, 255)
            
        # if the optional parameter is provided, then the color variable should be set to that
        if specificColor is not None:
            color = specificColor

        # creating a Rect object with the specific coordinates as per instance variables, and also making use of the static, consistent block widths
        currentBlock = Rect(self.x, self.y, Block.block_width, Block.block_width)

        # drawing the rect created above on the surface of the main pygame window
        pygame.draw.rect(Window, color, currentBlock)
        
        # updating the entire screen so that the new block drawn is visible
        pygame.display.flip()