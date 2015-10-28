# 6.8 The Egg Drop Problem: There is a building of 100 floors. If an egg drops
# from the Nth floor or above, it will break. If it's dropped from any floor
# below, it will not break. You're given two eggs. Find N, while minimizing the
# number of drops for the worst case.

# Here I denote floors from 0 to 99

import random
import math
import pdb

def brute_force():
	n = random.randint(0, 100)
	for i in range(100):
		if i == n:
			return i

def brute_binary_search():
	""" We use the first egg to do binary search, which is the most efficient. Once we
	break it, we use the second egg to do brute force search from low to high in the
	range which is determined by the previous binary search.

	Because we only have one egg left, we have to do brute force, that is, checking one
	by one, for that is our last and only chance.

	Then the number of drops for the worse case is 50, if the first drop in the middle
	breaks the egg.
	"""
	n = random.randint(0, 100)
	low = 0
	high = 99
	first_broken = False
	# use the first egg to do binary search
	while low <= high and not first_broken:
		mid = int((low+high)/2)
		if mid == n:
			return mid
		elif mid < n:
			low = mid + 1
		else:
			high = mid
			first_broken = True

	# use the second egg to do brute force search in [low, high]
	for i in range(low, high+1):
		if i == n:
			return i

def brute_binary_search_optimized():
	"""
	However, 50 still seems a large number to us. Seems that we spend too much time
	brute-force searching the lower part. Is it possible that we move the first
	check a little downwards so that 50 will be decreased? Sure, but how much?

	Assume the first drop floor is k.

	Let's observe the first drop. If it succeeds, the worst case is decided by how many
	times we do the binary search in the upper part, e.g. the depth of BST constructred
	by the upper part, which is int(log2(100-k)). If it succeeds, the worst case is decided
	by how many floors are in the lower part, which is k.

	Because we do not know whether it shall succeed or fail, we should consider both and
	try to reduce both.
	>>> brute_binary_search_optimized()
	"""

	worst_case_num_of_drops = [max(k, math.ceil(math.log2(100-k))) for k in range(100)]
	minimized_num_of_drops = min(worst_case_num_of_drops)
	N = worst_case_num_of_drops.index(minimized_num_of_drops)
	pdb.set_trace()
	return N, minimized_num_of_drops

if __name__ == "__main__":
	import doctest
	doctest.testmod()