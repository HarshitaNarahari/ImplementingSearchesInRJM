import heapq
import numpy as np
from VALID_MOVES import valid_moves

#Used the professor's code commented out below to complete this algorithm.
def H_score(node, goal, n):
	'''
	Fill in this function to return the heuristic value of the current node.

	Compute heuristic as the Manhattan distance between the 
	current node and the goal state, divided by 
	the largest possible jump value.

	n is the dimensionality of the maze (n x n).

	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''
	initial_x = node[0] 
	initial_y = node[1]
	goal_x = goal[0]
	goal_y = goal[1]
	# calculations based on instructions
	manhattan_distance = abs(initial_x - goal_x) + abs(initial_y - goal_y)
	largest_jump = n-1
	heuristic = manhattan_distance/largest_jump
	
	return heuristic


def ASTAR(maze, start, goal):
	visited = set()
	pqueue=[]
	heapq.heappush(pqueue, (H_score(start, goal, len(maze)), 0, (start, ())))
	while pqueue:
		# assigns heuristic, cost, (node, path) variables
		heuristic, cost, (node, path)=heapq.heappop(pqueue)
		path = path + (node, )
		if node == goal:
			return len(path)-1, path
		
		# finds neighboring nodes with valid moves function
		for neighbor in valid_moves(maze, node):
			if neighbor not in visited:
				edgeweight = 1
				new_row, new_col = neighbor
				G_score = cost + edgeweight # one jump equals 1 move
				heapq.heappush(pqueue, (G_score+H_score(neighbor, goal, len(maze)), G_score, (neighbor, path)))
				visited.add(node)


	#profs code
#	def astar(G, start, goal):
#	pqueue=[]
#	heapq.heappush(pqueue, (H_score(G, start, goal), 0, (start, ())))
#	while pqueue:
#		heuristic, cost, (node, path)=heapq.heappop(pqueue)
#		path = path + (node)
#		if node==goal:
#			return path
#		for neighbor, edgeweight in G[node].items():
#			G_score = cost + edgeweight
#			heapq.heappush(pqueue, (G_score+H_score(G, neighbor, goal), G_score, (neighbor, path)))

	'''
	Fill in this function that uses A* search to find the shortest 
	path using the heuristic function H_score defined above.

	Return the length of the shortest path from the start state 
	to the goal state, and the path itself.

	Your return statement should be of the form:
	return len(path)-1, path

	where path is a list of tuples, corresponding to the 
	path and includes the start state.

	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''


