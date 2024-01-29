import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR
from HILLDESCENT import energyfunction

def SIMULATED_ANNEALING(maze, start_cell, goal_state, iterations, T, decay):
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
			
			# put inside the function so the value can be updated for each iteration
			if best_energy > neighbor_energy:
				probability_exp = (best_energy - neighbor_energy)/T
			else:
				probability_exp = 1

			# lower energy means better algorithm, so replaces the values to find best path
			if neighbor_energy < best_energy:
				start_cell = rand_cell
				best_energy = neighbor_energy

			# if new energy is greater than best energy, move to that cell with probability exp
			if neighbor_energy > best_energy:
				if np.random.uniform(0.0, 1.0, size=None) < np.exp(probability_exp):
					start_cell = rand_cell
					best_energy = neighbor_energy

			else:
				best_maze[rand_cell] = saved_cell
				# decrease temp
		
		# decrements T by decay value
		T *= decay
		# decrements iterations after every iteration
		iterations = iterations - 1
				
	return best_solution
	
	'''
	Fill in this function to implement Simulated Annealing.

	The energy function is the same as used for Hill Descent
	and is already imported here for it to be used directly
	(see the energyfunction() function in HILLDESCENT.py).

	With an input temperature 'T' and a decay rate 'decay',
	you should run the algorithm for 'iterations' steps.

	At each step, you should randomly select a valid move,
	and move to that state with probability 1 if the energy
	of the new state is less than the energy of the current state,
	or with probability exp((current_energy - new_energy)/T)
	if the energy of the new state is greater than the current energy.

	After each step, decrease the temperature by 
	multiplying it by the decay rate.

	Your function should return the best solution found,
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''


