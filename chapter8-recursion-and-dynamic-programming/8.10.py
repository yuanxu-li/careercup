# 8.10 Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# fill in the surrounding area until the color changes from the original color.

def paint_fill(array, point, color, memo=None):
	"""
	>>> paint_fill([[4, 5, 7, 3, 8, 4], [3, 6, 2, 9, 4, 0], [0, 6, 0, 2, 6, 3], [1, 2, 0, 0, 0, 4]], (1, 1), 0)
	True
	"""
	# alternative for initial call
	if memo is None:
		memo = set()

	# visited before, return
	if point in memo:
		return True
	# otherwise, change the color of this point, and recursively change its neighbors
	array[point[0]][point[1]] = color
	memo.add(point)
	if point[0] < len(array) - 1:
		paint_fill(array, (point[0]+1, point[1]), color, memo)
	if point[1] < len(array[0]) - 1:
		paint_fill(array, (point[0], point[1]+1), color, memo)
	if point[0] > 0:
		paint_fill(array, (point[0]-1, point[1]), color, memo)
	if point[1] > 0:
		paint_fill(array, (point[0], point[1]-1), color, memo)
	return True

if __name__ == "__main__":
	import doctest
	doctest.testmod()
