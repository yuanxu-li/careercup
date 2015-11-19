# 8.10 Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# fill in the surrounding area until the color changes from the original color.

def paint_fill(array, row, col, new_color, old_color=None):
	"""
	>>> array = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]]
	>>> paint_fill(array, 1, 3, 9)
	True
	>>> array
	[[9, 9, 9, 9], [9, 9, 9, 9], [1, 1, 1, 1], [1, 1, 1, 1]]
	"""
	# alternative for initial call
	if old_color is None:
		old_color = array[row][col]

	# if the point is off limit
	if row < 0 or row >= len(array) or col < 0 or col >= len(array[0]):
		return False
	# if arrives at the border of old color
	if array[row][col] != old_color:
		return True
	# change the color of this point, and recursively change its neighbors
	array[row][col] = new_color
	paint_fill(array, row+1, col, new_color, old_color)
	paint_fill(array, row, col+1, new_color, old_color)
	paint_fill(array, row-1, col, new_color, old_color)
	paint_fill(array, row, col-1, new_color, old_color)
	return True

if __name__ == "__main__":
	import doctest
	doctest.testmod()
