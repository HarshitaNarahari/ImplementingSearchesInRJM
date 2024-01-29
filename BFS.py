import numpy as np
from VALID_MOVES import valid_moves


# https://numpy.org/doc/stable/reference/arrays.ndarray.html - used to understand how to code 2D arrays
def BFS(maze, start):
    queue = []
    visited = set()
    # fill with -1's to check this later:  if no path exists from the start state to a given cell
    path_matrix = np.full((len(maze), len(maze)), -1, dtype=int)
    
    start_row, start_col = start
    # The start state should be assigned a path length of 0.
    path_matrix[start] = 0
    queue.append(start)
    
    while queue:
        current_node = queue.pop(0)
        #checks for valid moves aka the neighbors
        neighbors = valid_moves(maze, current_node)
        
        for neighbor in neighbors:
            if path_matrix[neighbor] == -1:
                path_matrix[neighbor] = path_matrix[current_node] + 1
                queue.append(neighbor)
    
    return path_matrix


    # '''
    # Fill in this function that uses Breadth First Search to find the shortest path 
    # from the start state to the goal state.
    
    # Return the matrix (a 2-dimensional numpy array) of shortest path 
    # distances from the start cell to each cell. 
    
    # If no path exists from the start state to a given cell, that cell should be assigned -1.
    
    # The start state should be assigned a path lenght of 0.
    
    # If using print statements to debug, please make sure 
    # to remove them before your final submisison.
    # '''
