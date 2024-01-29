def valid_moves(maze, node):
	neighbors=[]
	
	'''
	Fill in this function to return a list of "valid" neighbors 
	for the current node in the rook-jumping-maze.
	
	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''
	
	# start node
	x_coordinate = node[0]
	y_coordinate = node[1]
	node_size = maze[x_coordinate][y_coordinate]
	dim = len(maze)

	# Boundaries established using maze's height and width
	# checks if the node the algorithm is exploring is reachable
	if x_coordinate + node_size < dim:
		neighbors.append((x_coordinate + node_size, y_coordinate))
	if x_coordinate - node_size >= 0:
		neighbors.append((x_coordinate - node_size, y_coordinate))
	if y_coordinate + node_size < dim:
		neighbors.append((x_coordinate, y_coordinate + node_size))
	if y_coordinate - node_size >= 0:
		neighbors.append((x_coordinate, y_coordinate - node_size))
	
	return neighbors





