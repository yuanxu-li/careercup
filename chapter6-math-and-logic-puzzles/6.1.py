# 6.1 The Heavy Pill: You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but
# one has pills of weight 1.1 grams. Given a scale that provides an exact measurement,
# how would you find the heavy bottle?
# You can only use the scale once.

import pdb

def find_heavy_bottle(bottles):
	"""
	We are only allowed to use the scale once, which means we have to use all the bottles.
	By putting the pills on the scale, we are able to see which side is heavier, but how can
	we track from which bottle the pills lead to the heavier side?

	The approach is to use the difference of weights on both sides to infer which bottle
	We number the bottles from 0 to 19, and we take i pills from each bottle,
	and weigh it. The number is decided by the formula:
	(weight - 190) / 0.1

	>>> find_heavy_bottle([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.1, 1])
	18
	>>> find_heavy_bottle([1.1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	0
	"""
	return round((sum([i * v for i, v in enumerate(bottles)]) - 190) / 0.1)

if __name__ == "__main__":
	import doctest
	doctest.testmod()