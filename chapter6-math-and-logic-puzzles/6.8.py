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

drops = 0
break_floor = 20
def drop(floor):
	global drops
	drops += 1
	return floor >= break_floor

def find_breaking_floor(k):
	""" When we use egg1, we could skip floors each time and reduce the range, like when we drop egg1 from 10th floor it is Ok,
	but broken from 20th floor, then we should search from 11th floor through 19th floor using egg2. Because egg2 is our last choice,
	we should use the safest linear search. Then how should we minimize the total number of drops for the worst case?
	The idea to keep drops(egg1) + drops(egg2) steady, meaning to keep the worst case almost the same as the best case. Then each time
	we drop egg1 one more time adding drop(egg1) by 1, we should reduce the increment by 1 thus reducing drop(egg2) by 1.
	>>> find_breaking_floor(30)
	30
	>>> find_breaking_floor(50)
	50
	>>> find_breaking_floor(70)
	70
	"""
	global break_floor
	global drops
	break_floor = k
	interval = 14
	previous = 0
	egg1 = interval
	drops += 1
	# drop egg1
	while not drop(egg1) and egg1 <= 100:
		interval -= 1
		previous = egg1
		egg1 += interval
	# drop egg2
	egg2 = previous + 1
	while egg2 < egg1 and egg2 <= 100 and not drop(egg2):
		egg2 += 1

	return -1 if egg2 > 100 else egg2


if __name__ == "__main__":
	import doctest
	doctest.testmod()