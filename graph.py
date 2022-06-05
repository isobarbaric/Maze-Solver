
from .block import Block

class Graph:

    def __init__(self, grid):
        # storing the grid in a variable
        self.grid = grid
        
        # creating a dictionary to store the adjacency list for the Graph, in a form of a one-to-one mapping style graph
        self.adj_list = dict()
        
        # calling the create_graph() method 
        self.create_graph()
    
    def create_graph(self):
        # creating two lists to store the deviation in terms of the x-coordinates and y-coordinates from the current grid cell
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        
        # looping through all of the y-coordinates
        for y in range(len(self.grid)):
            # looping through all of the x-coordinates
            for x in range(len(self.grid[y])):
                # looping through the four possible deviations
                for d in range(4):
                    # if the y-coordinate is out of bounds, skip the current iteration
                    if (y + dy[d] >= len(self.grid) or y + dy[d] < 0):
                        continue

                    # if the x-coordinate is out of bounds, skip the current iteration 
                    if (x + dx[d] >= len(self.grid[y]) or x + dx[d] < 0):
                        continue

                    # if the current cell is a wall, then there shouldn't be a graph for it, and so such cells will be skipped by this if-statement
                    if self.grid[y + dy[d]][x + dx[d]].isWall:
                        continue

                    # store the current coordinates as a tuple
                    curr = (y + dy[d], x + dx[d])

                    # case-wise consideration based on whether the current coordinates exist as a key or not in the adjacency list
                    if not (y, x) in self.adj_list:
                        # if the adjacency list does not have the current coordinates as a key, then create that key and corresponding value
                        self.adj_list[(y, x)] = [curr]
                    else:
                        # if the adjacency list does contain the current coordinates as a key, then simply append to that list of values 
                        self.adj_list[(y, x)].append(curr)