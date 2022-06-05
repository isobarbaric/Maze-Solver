
import time
import pygame

from .block import Block
from .graph import Graph 
from .maze import maze_generator
from .GUI import GUI

class MazeSolver:

    # creating a variable to keep track of the size of window to create for the pygame GUI
    window_size = 650

    def __init__(self):

        # initializing a list to store a grid of blocks involved in the maze
        self.blocks = []
        
        # initializing a dictionary to store the previous node for every node explored during the graph traversal
        self.parent_node = dict()
        
        # initializing a list to store visited nodes
        self.visited = []
        
        # initializing a variable to keep track of the size of thr maze 
        self.sz = GUI().main()
        
        # setting the block width for the Block class accordingly as per the size of the maze determined
        Block.block_width = (MazeSolver.window_size - (self.sz + 1) * Block.wall_width)/self.sz

    def create_grid(self, generated_maze):
        # looping over the y-coordinates
        for y in range(1, self.sz+1):
            # creating a new list inside the list to store the elements in the y-th row 
            self.blocks.append([])
            
            # looping over the x-coordinates
            for x in range(1, self.sz+1):
                # creating a variable to track a Block object's isWall instance variable 
                isWall = True

                # if the particular cell in question is a cell and not a wall, then mark things accordingly 
                if (generated_maze[y-1][x-1] == 'c'):
                    # setting the isWall variable to false in the case that the cell in question is not a wall 
                    isWall = False

                # creating a Block object considering the appropriate widths and sizes of the Block objects and the walls between them 
                currentBlock = Block(Block.wall_width*x + Block.block_width*(x-1), Block.wall_width*y + Block.block_width*(y-1), isWall)

                # adding this to the blocks grid in the current row 
                self.blocks[-1].append(currentBlock)

    def draw_blocks(self, WINDOW):
        # drawing the blocks in each row 
        for row in self.blocks:
            # accessing each element as a part of a row in the grid
            for elem in row:
                # calling the draw method on each block 
                elem.draw(WINDOW)
                
                # pausing the program after each individual block is drawn to slow down the rate at which they are drawn to make it seem more natural
                time.sleep(0.005)

        # updating the pygame display to reflect the changes of drawing blocks on it
        pygame.display.update()

    def graph_traversal(self):
        # creating a Graph object from a grid of blocks
        block_graph = Graph(self.blocks)    
        
        # creating a variable to store the starting node in the maze
        self.start_node = (0, 1)
        
        # looping through the first row of the maze to find the starting point
        for i in range(self.sz):
            # if the current cell in the first row contains a 'c', this means that that cell is the starting point for the maze 
            if (self.random_maze[0][i] == 'c'):
                # if the starting node in the maze is found, set the start_node variable accordingly and break
                self.start_node = (0, i)
                break 
        
        # running the depth-first search algorithm on the graph
        self.depth_first_search(self.start_node, block_graph)

    def depth_first_search(self, current_node, block_graph):
        # looping through the other nodes in the current node's adjacency list to find new unexplored nodes
        for other_node in block_graph.adj_list[(current_node[0], current_node[1])]:
            # if an unexplored node is found, it is marked as being explored and its neighbors are then searched for 
            if other_node not in self.visited:
                # mark the node as visited 
                self.visited.append(other_node)
        
                # mark the parent of the current node so that the algorithm's path can be traced
                self.parent_node[other_node] = current_node
        
                # call the depth-first search algorithm on the current node to explore its adjacent nodes
                self.depth_first_search(other_node, block_graph)

    def generate_path(self):
        # creating a variable to store the ending node in the maze
        last_node = (self.sz-1, self.sz-2)
       
        # looping through the last row of the maze to find the ending point
        for i in range(self.sz):
            # if the current cell in the last row contains a 'c', this means that that cell is the ending point for the maze 
            if (self.random_maze[-1][i] == 'c'):
                # if the ending node in the maze is found, set the last_node variable accordingly and break
                last_node = (self.sz-1, i)
        
        # creating a list to store the path that the depth-first search algorithm took from start to end   
        path_list = []
        
        # creating a variable to store the current node and initializing it by assigning it the value of the last node determined above 
        current_node = last_node
        
        # going backwards to find the path that the depth-first search algorithm took in finding the path from the starting point to the ending point in the maze 
        while current_node != self.start_node:
            # adding the current node to the list of nodes in the path
            path_list.append(current_node)
        
            # moving the current node back to recursively compute its parent
            current_node = self.parent_node[current_node]
        
        # edge case in the above looping is that the start node is not added to the path list, for that reason, adding it manually deals with the edge case 
        path_list.append(self.start_node)
        
        # as this path list generated is backwards, reversing it will give the correct path from start to end 
        path_list.reverse()
        
        # returning the path (in the form of coordinates) from beginning to end in the maze
        return path_list

    def draw_path(self, WINDOW):
        # start a graph traversal for the current maze, which in turn will call DFS
        self.graph_traversal()
        
        # coloring the path the algorithm took on the grid
        for elem in self.generate_path():
            # setting the blocks in concern on the path to the color green to distinguish them 
            self.blocks[elem[0]][elem[1]].draw(WINDOW, (0, 255, 0))
            
            # pausing the program after each individual block is colored to slow down the rate at which they are drawn to make it seem more natural
            time.sleep(0.1)
        
        # updating the pygame display to reflect the changes of setting some blocks to a different color
        pygame.display.update()

    def main(self):
        # initialize pygame to start making the game window
        pygame.init()
        
        # giving the pygame window a releavant
        pygame.display.set_caption("Maze Solver")
        
        # creating a window for pygame to display in according to the static, consistent window_size defined above 
        WINDOW = pygame.display.set_mode((MazeSolver.window_size, MazeSolver.window_size))
        
        # setting the color of the window to black for the animation-like effect when the window is
        WINDOW.fill((0, 0, 0)) 
        
        # generating a random maze
        self.random_maze = maze_generator(self.sz)  
        
        # creating a grid of blocks based on the random maze generated
        self.create_grid(self.random_maze) 
        
        # drawing the grid of blocks generated one line above
        self.draw_blocks(WINDOW)
        
        # making the pygame window remain unchanged for a brief moment before the path is highlighted
        time.sleep(1)
        
        # drawing the path the algorithm took and displaying this to the user 
        self.draw_path(WINDOW)   
        
        # boolean variable to allow the game to be played
        continuePlaying = True
        
        # a while loop to run the game
        while continuePlaying:
            # makes sure the game goes about at the desired frame rate
            for event in pygame.event.get():
                # if the user wishes to quit the game, the continuePlaying boolean will be marked to false, causing the while loop to terminate
                if event.type == pygame.QUIT:
                    continuePlaying = False
        
        # quit the game once the quit button is pushed
        pygame.quit()