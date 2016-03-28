# 16.3 Intersection: Given two straight line segments (represented as a start point
# and an end point), compute the point of intersection, if any

def point_of_intersection(point1, point2, point3, point4):
	"""
	Reference: http://www-cs.ccny.cuny.edu/~wolberg/capstone/intersection/Intersection%20point%20of%20two%20lines.html
	>>> point_of_intersection((0, 2), (2, 0), (0, 1), (3, 0))
	(1.5, 0.5)
	>>> point_of_intersection((0, 2), (2, 0), (2, 1), (5, 0))
	"""
	denominator = (point4[1] - point3[1]) * (point2[0] - point1[0]) - (point4[0] - point3[0]) * (point2[1] - point1[1])
	a_numerator = (point4[0] - point3[0]) * (point1[1] - point3[1]) - (point4[1] - point3[1]) * (point1[0] - point3[0])
	b_numerator = (point2[0] - point1[0]) * (point1[1] - point3[1]) - (point2[1] - point1[1]) * (point1[0] - point3[0])

	# parallel
	if denominator == 0:
		# coincident
		if a_numerator == 0 and b_numerator == 0:
			# line segments overlapping
			if (point1[0] <= point3[0] <= point2[0] <= point4[0] or point1[0] >= point3[0] >= point2[0] >= point4[0]) and \
				(point1[1] <= point3[1] <= point2[1] <= point4[1] or point1[1] >= point3[1] >= point2[1] >= point4[1]):
				return point3
			# line segments not overlapping
			else:
				return None
		# parallel but not coincident
		else:
			return None
	# not parallel
	else:
		u_a = a_numerator / denominator
		u_b = b_numerator / denominator
		# intersection within line segments
		if 0 <= u_a <= 1 and 0 <= u_b <= 1:
			return (point1[0] + u_a * (point2[0] - point1[0]), point1[1] + u_a * (point2[1] - point1[1]))
		# intersection beyond line segments
		else:
			return None


if __name__ == "__main__":
	import doctest
	doctest.testmod()



