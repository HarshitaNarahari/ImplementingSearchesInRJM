import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR
import random

# https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=4a94d5ad330286464385f217d7ed2c58321f7459
# used the pseudocode in the link above to figure out the hill descent functions below

def energyfunction(maze, start, goal):
	'''
	Compute the energy as the sum of the shortest path length 
	from the start state to the goal state (computed using A*)
	and the number of cells that are not reachable from the 
	start state (computed using BFS).

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''

	shortest_length = ASTAR(maze, start, goal)[0]
	non_reachable_cells = np.sum(BFS(maze, start)==-1) #count the -1(unreachable) cells
	energy = shortest_length + non_reachable_cells
	return energy


def HILLDESCENT(maze, start_cell, goal_state, iterations):
	best_maze = maze.copy()
	best_energy = energyfunction(maze, start_cell, goal_state)
	best_solution = (best_maze, best_energy)
	dim = len(maze)
	
	# while there are still more iterations to run
	while 0 < iterations:
		random_move = np.random.randint(1, dim)
		# pick a cell
		rand_cell = (np.random.randint(0, dim), np.random.randint(0, dim))
		
		# make sure it's not the goal state
		if best_maze[rand_cell] != 0:
			# changes the cell
			saved_cell = best_maze[rand_cell]
			best_maze[rand_cell] = random_move

			# try catch for mazes without solutions
			try:
				neighbor_energy = energyfunction(best_maze, start_cell, goal_state)
			except:
				continue

			# lower energy means better algorithm, so replaces the values to find best path
			if neighbor_energy < best_energy:
				start_cell = rand_cell
				best_energy = neighbor_energy
			else:
				best_maze[rand_cell] = saved_cell

		# decrements iterations after every iteration
		iterations = iterations - 1
	return best_solution


	'''
	Fill in this function to implement Hill Descent local search.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze 
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''


# iterations of hill descent differ with different explorations - best out of multiple trials
def HILLDESCENT_RANDOM_RESTART(maze, start_cell, goal_state, iterations, num_searches):

	best_maze = maze.copy()
	seperate_maze = maze.copy()
	best_energy = energyfunction(maze, start_cell, goal_state)
	best_solution = (best_maze, best_energy)
	dim = len(maze)
	
	# while there are still more searches to run
	while 0 < num_searches: 
		# while there are still more iterations to run
		while 0 < iterations:
			random_move = np.random.randint(1, dim)
			# pick a cell
			rand_cell = (np.random.randint(0, dim), np.random.randint(0, dim))
		
			# make sure it's not the goal state
			if best_maze[rand_cell] != 0:
				# changes the cell
				saved_cell = best_maze[rand_cell]
				best_maze[rand_cell] = random_move

				# try catch for mazes without solutions
				try:
					neighbor_energy = energyfunction(best_maze, start_cell, goal_state)
				except:
					continue

				# lower energy means better algorithm, so replaces the values to find best path
				if neighbor_energy < best_energy:
					start_cell = rand_cell
					best_energy = neighbor_energy
				else:
					best_maze[rand_cell] = saved_cell
			
			# decrements iterations after every iteration
			iterations = iterations - 1
		# decrements num_searches after every search
		num_searches = num_searches - 1
	
	return best_solution

	'''
	Fill in this function to implement Hill Descent local search with Random Restarts.

	For a given number of searches (num_searches), run hill descent search.

	Keep track of the best solution through all restarts, and return that.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze 
	before making any changes to it.

	You will also need to keep a separate copy of the original maze
	to use when restarting the algorithm each time.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''

def HILLDESCENT_RANDOM_UPHILL(maze, start_cell, goal_state, iterations, probability):
	best_maze = maze.copy()
	best_energy = energyfunction(maze, start_cell, goal_state)
	best_solution = (best_maze, best_energy)
	dim = len(maze)
	
	while 0 < iterations:
		random_move = np.random.randint(1, dim)
		# pick a cell
		rand_cell = (np.random.randint(0, dim), np.random.randint(0, dim))
		
		# make sure it's not the goal state
		if best_maze[rand_cell] != 0:
			# changes the cell
			saved_cell = best_maze[rand_cell]
			best_maze[rand_cell] = random_move

			# try catch for mazes without solutions
			try:
				neighbor_energy = energyfunction(best_maze, start_cell, goal_state)
			except:
				continue

			# lower energy means better algorithm, so replaces the values to find best path
			if neighbor_energy < best_energy:
				start_cell = rand_cell
				best_energy = neighbor_energy
			
			# generates a random number between 1 and 0 to test probability
			if np.random.uniform(0.0, 1.0, size=None) < probability:
				start_cell = rand_cell
				best_energy = neighbor_energy

			else:
				# revert if the previous cell was a part of a more optimal path for the maze
				best_maze[rand_cell] = saved_cell

		# decrements iterations after every iteration
		iterations = iterations - 1
				
	return best_solution

	'''
	Fill in this function to implement Hill Descent local search with Random uphill steps.

	At each iteration, with probability specified by the probability
	argument, allow the algorithm to move to a worse state.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''






