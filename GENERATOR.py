import sys
import numpy as np
from BFS import BFS

def generator(k):
	# size of maze
	size = (k, k)
	# random maze
	init_board = np.random.randint(1, k, (size))
	
	# generates random start_cell and goal_state
	start_cell = (np.random.randint(0,k), np.random.randint(0,k))
	goal_state = (np.random.randint(0,k), np.random.randint(0,k))
	
	# ensure that start_cell and goal_state are not the same
	while start_cell == goal_state:
		goal_state = (np.random.randint(0,k), np.random.randint(0,k))
	
	# Sets the entry in the maze corresponding to the goal state to 0
	init_board[goal_state] = 0

	return init_board, start_cell, goal_state


	'''
	Fill in this function to generate a k * k maze with random 
	integers between 1 and k-1 (included) in each cell.
	
	Generate a random start state and a random goal state.
	Each of these should be a tuple of integers.
	
	Make sure that the start state and the goal state are not the same.
	
	Set the entry in the maze corresponding to the goal state to 0.
	
	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''


def generator_pathcheck(k):
	# init_board generates a maze
	init_board = generator(k)

	maze = init_board[0]
	start_cell = init_board[1]
	goal_state = init_board[2]

	# checks if if there is a path from the start state to the goal state
	while BFS(maze, start_cell)[goal_state] == -1:
		return generator_pathcheck(k)

	return maze, start_cell, goal_state


	'''
	Copy above function here and modify as follows:
	
	Once a maze is generated, use BFS to check if there is 
	a path from the start state to the goal state.
	
	If there is a valid path, return the maze, the start state, and the goal state.
	
	If not, generate a new maze and repeat.
	'''






	