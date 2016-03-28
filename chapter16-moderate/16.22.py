# 16.22 Langton's Ant: An ant is sitting on an infinite grid of white and black squares.
# It initially faces right. At each step, it does the following:
# (1) At a white square, flip the color of the square, turn 90 degrees right (clockwise),
# and move forward one unit.
# (2) At a black square, flip the color of the square, turn 90 degrees left (counter-clockwise),
# and move forward one unit.
# Write a program to simulate the first K moves that the ant makes and print the final board
# as a grid. Note that you are not provided with the data structure to represent the grid.
# This is something you must design yourself. The only input to your method is K. You should
# print the final grid and return nothing. The method signature might be something like
# void printKMoves(int K).

def print_k_moves(k):
	"""
	We use dict to store all passed squares. Each step, if the touched square is not visited yet, then
	append it to the dict; if already visited, change the status of that square in dict. For each new square,
	if the sum of x and y axis is even, it is white(represented by 0); otherwise, it is black(represented by 1).
	The direction is represented as 0(right), 1(down), 2(left), 3(up).
	>>> print_k_moves(5)
	[[1, 1, 0], [0, 1, 1], [0, 0, 1], [1, 0, 1]]
	"""
	grid = {}
	# assume the ant starts with a white square at (0, 0)
	cur = (0, 0)
	grid[cur] = sum(cur) % 2
	direction = 0

	# move k steps
	for i in range(k):
		# flip color
		# white: in grid and color is white or not in grid but is supposed to be white
		if cur in grid and grid[cur] == 0 or cur not in grid and sum(cur) % 2 == 0:
			grid[cur] = 1
			direction = (direction + 1) % 4
		# black: otherwise
		else:
			grid[cur] = 0
			direction = (direction - 1) % 4
		# move forward one unit
		if direction == 0:
			cur = (cur[0], cur[1] + 1)
		elif direction == 1:
			cur = (cur[0] + 1, cur[1])
		elif direction == 2:
			cur = (cur[0], cur[1] - 1)
		elif direction == 3:
			cur = (cur[0] - 1, cur[1])
		else:
			raise Exception("Undefined direction value!")
	# also append the last
	if cur not in grid:
		if sum(cur) % 2 == 0:
			grid[cur] = 0
		else:
			grid[cur] = 1

	# print out the final grid
	# x-axis is vertical downward while y-axis is horizontal rightward.

	x_max = max(p[0] for p in grid)
	x_min = min(p[0] for p in grid)
	y_max = max(p[1] for p in grid)
	y_min = min(p[1] for p in grid)

	# we use a 2-d array to represent the grid as the result to be returned
	result = []

	for x in range(x_min, x_max+1):
		row = []
		for y in range(y_min, y_max+1):
			if (x, y) in grid:
				row.append(grid[(x, y)])
			else:
				if (x + y) % 2 == 0:
					row.append(0)
				else:
					row.append(1)
		result.append(row)
	return result

if __name__ == "__main__":
	import doctest
	doctest.testmod()
