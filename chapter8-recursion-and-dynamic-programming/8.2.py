# 8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the
# bottom right

def move_robot(maze, position=(0, 0)):
	""" A recursive method is employed here. At one cell, we can choose either down or right, and decide
	the right routine according to the returned path(None for wrong path). And whether the right or down way
	works out is decided recursively. If neither down nor right works out, we mark this cell as False in order
	that other paths don't have to search from this.
	>>> maze = [[True for i in range(10)] for j in range(15)]
	>>> maze[3][5], maze[4][5], maze[5][5], maze[5][3], maze[5][4], maze[5][3], maze[0][4], maze[1][4] \
	= False, False, False, False, False, False, False, False
	>>> move_robot(maze)
	[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9)]
	"""
	# if the current cell is off limit
	if position[0] >= len(maze) or position[1] >= len(maze[0]) or maze[position[0]][position[1]] is False:
		return None
	# if arrive at the bottom right corner
	elif position[0] == len(maze)-1 and position[1] == len(maze[0])-1:
		return [position]
	else:
		# try right
		path = move_robot(maze, (position[0], position[1]+1))
		if path is not None:
			path.append(position)
			return path
		# try down
		path = move_robot(maze, (position[0]+1, position[1]))
		if path is not None:
			path.append(position)
			return path
		# if neither right nor down works out, mark this position as False and return None
		maze[position[0]][position[1]] = False
		return None

def move_robot_updated(maze, row=None, col=None, memo=None):
	""" Instead of searching from the origin, we recursively start searching from the destination. By keeping
	all visited points in a memo, we do not repeating paths.
	>>> maze = [[True for i in range(10)] for j in range(15)]
	>>> maze[3][5], maze[4][5], maze[5][5], maze[5][3], maze[5][4], maze[5][3], maze[0][4], maze[1][4] \
	= False, False, False, False, False, False, False, False
	>>> move_robot_updated(maze)
	"""
	# alternative for initial call
	if row is None or col is None or memo is None:
		row = len(maze) - 1
		col = len(maze[0]) - 1
		memo = set()

	# if find the origin, return itself as the path
	if row == 0 and col == 0:
		return [(row, col)]

	# if the point has beeen 
	if (row, col) in memo or not maze[row][col] or row < 0 or col < 0:
		return None

	# try coming from up
	path = move_robot_updated(maze, row - 1, col, memo)
	if path is not None:
		path.append((row, col))
		return path
	# try coming from left
	path = move_robot_updated(maze, row, col - 1, memo)
	if path is not None:
		path.append((row, col))
		return path
	# if neither direction works out, mark this position as visited
	memo.add((row, col))
	return None







if __name__ == "__main__":
	import doctest
	doctest.testmod()