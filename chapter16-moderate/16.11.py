# 16.11 Diving Board: You are building a diving board by placing a bunch of planks of wood
# end-to-end. There are two types of planks, one of length shorter and one of length longer.
# You must use exactly K planks of wood. Write a method to generate all possible lengths for
# the diving board.

def all_possible_lengths(a, b, k):
	"""
	a: shorter length
	b: longer length
	k: number of planks of wood
	each time we change a plank of wood of shorter length for one of longer length, the length of
	diving board changes by the difference of the shorter length and the longer length. Therefore,
	we can count from the situation of all shorter lengths, change one shorter plank for a longer one,
	until all are planks of longer length.
	>>> all_possible_lengths(3, 8, 30)
	[90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240]
	>>> all_possible_lengths(3, 6, 4)
	[12, 15, 18, 21, 24]
	"""
	lengths = []
	cur = a * k
	lengths.append(cur)
	diff = b - a
	for i in range(k):
		cur += diff
		lengths.append(cur)
	return lengths

if __name__ == "__main__":
	import doctest
	doctest.testmod()