# 16.13 Bisect Squares: Given two squares on a two-dimensional plane, find a line that
# would cut these two squares in half. Assume that the top and the bottom sides of the
# square run parallel to the x-axis.

class Square:
	def __init__(self, *points):
		self.points = points

	def center(self):
		return (sum(point[0] for point in self.points) / len(self.points), \
			sum(point[1] for point in self.points) / len(self.points))

def bisecting_line(s1, s2):
	"""
	Define a line as ax+by+c=0, return a, b, c
	>>> s1 = Square((-1, 3), (1, 3), (-1, 1), (1, 1))
	>>> s2 = Square((1, 1), (3, 1), (1, -1), (3, -1))
	>>> bisecting_line(s1, s2)
	(1.0, 1, -2.0)
	"""
	c1 = s1.center()
	c2 = s2.center()
	if c1[0] == c2[0]:
		return 1, 0, -c1[0]
	elif c1[1] == c2[1]:
		return 0, 1, -c1[1]
	else:
		return (c2[1] - c1[1]) / (c1[0] - c2[0]), 1, (c1[0] * c2[1] - c2[0] * c1[1]) / (c2[0] - c1[0])

if __name__ == "__main__":
	import doctest
	doctest.testmod()