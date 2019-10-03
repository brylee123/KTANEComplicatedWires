import maze_design

def find_path(graph, start_vertex, end_vertex, path=None):
	if path == None:
		path = []
	path = path + [start_vertex]
	#print(path)
	if start_vertex == end_vertex:
		return path
	for vertex in graph[start_vertex]:
		if vertex not in path:
			extended_path = find_path(graph, vertex, end_vertex, path)
			if extended_path: 
				return extended_path
	return None

def coord_validation(input_coord):
	if input_coord.count(",") > 1 or "," not in input_coord:
		print("Error: Incorrect coordinate formatting.")
		return 0
	x, y = input_coord.replace(" ", "").split(",")
	if not x.isnumeric() or not y.isnumeric() or int(x) > 6 or int(x) < 1 or int(y) > 6 or int(y) < 1:
		print("Error: x or y coordinate is not a valid integer or it is not within range")
		return 0
	return (int(x), int(y))
	
def maze():

	valid_indicators = {
		(1,5): 1, (6,4): 1,
		(2,3): 2, (5,5): 2,
		(4,3): 3, (6,3): 3,
		(1,3): 4, (1,6): 4,
		(4,1): 5, (5,4): 5,
		(3,2): 6, (5,6): 6,
		(2,1): 7, (2,6): 7,
		(3,3): 8, (4,6): 8,
		(1,2): 9, (3,5): 9
	}

	indicator_input = ""
	indicator = None
	while indicator not in valid_indicators.keys():
		indicator_input = input("Input one indicator coordinate (green circle): ")
		indicator = coord_validation(indicator_input)
		if indicator == 0: # Returned error
			continue
		if indicator not in valid_indicators.keys():
			print("Error: Cooridinate does not match any existing mazes. Try again.")
	maze_number = valid_indicators[indicator]

	# At this point, the maze should be chosen and decided upon

	curloc_input = ""
	curloc = None
	while 1:
		curloc_input = input("What is the coordinate of current location (white square): ")
		curloc = coord_validation(curloc_input)
		if curloc != 0: # coord_validation returns 0 if there is an error
			break

	target_input = ""
	target = None
	while 1:
		target_input = input("What is the coordinate of target location (red triange): ")
		target = coord_validation(target_input)
		if target != 0: # coord_validation returns 0 if there is an error
			break

	adj_list = maze_design.maze_design(maze_number) # Insert correct graph number

	path = find_path(adj_list, curloc, target)

	relative_path = []
	for i, cur_node in enumerate(path): # Translate path to relative directions
		if cur_node == curloc: # First
			continue
		else:
			px, py = path[i-1] # Previous Node
			cx, cy = cur_node # Current Node

			if cx > px:
				relative_path.append("RIGHT")
			elif cx < px:
				relative_path.append("LEFT")
			elif cy > py:
				relative_path.append("UP")
			elif cy < py:
				relative_path.append("DOWN")

	print(relative_path)

if __name__ == '__main__':
	maze()