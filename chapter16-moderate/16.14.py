# 16.14 Best Line: Given a two-dimensional graph with points on it, find a line which passes
# the most number of points.

from collections import defaultdict

class Line:
	def __init__(self, point1, point2):
		self.point1 = point1
		self.point2 = point2
		self.compute_parameters()
		self.count = 1

	def compute_parameters(self):
		if self.point1[0] == self.point2[0]:
			self.a = 1
			self.b = 0
			self.c = self.point1[0]
		elif self.point1[1] == self.point2[0]:
			self.a = 0
			self.b = 1
			self.c = self.point1[1]
		else:
			self.a = (self.point2[1] - self.point1[1]) / (self.point1[0] - self.point2[0])
			self.b = 1
			self.c = (self.point2[0] * self.point1[1] - self.point1[0] * self.point2[1]) / (self.point2[0] - self.point1[0])

	def __repr__(self):
		return "|".join([str(self.a), str(self.b), str(self.c)])

	def __hash__(self):
		return hash(self.__repr__())

	def __eq__(self, other):
		return self.a == other.a and self.b == other.b and self.c == other.c

	def __ne__(self, other):
		return self.a != other.a or self.b != other.b or self.c != other.c

def line_with_most_points(*points):
	"""
	>>> line = line_with_most_points((0, 2), (1, 1), (2, 0), (3, 0), (4, 0))
	>>> line.a
	-0.0
	>>> line.b
	1
	>>> line.c
	0.0
	>>> line = line_with_most_points((0, 2), (1, 1), (2, 0), (3, -1), (4, -2), (9, 12))
	>>> line.a
	1.0
	>>> line.b
	1
	>>> line.c
	2.0
	"""
	d = defaultdict(int)
	for i in range(len(points)-1):
		for j in range(i+1, len(points)):
			d[Line(points[i], points[j])] += 1
	return max(d, key=lambda k: d[k])

if __name__ == "__main__":
	import doctest
	doctest.testmod()