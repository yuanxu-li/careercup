# 8.6 Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers
# and N disks of different sizes which can slide onto any tower. The puzzle starts with
# disks sorted in ascending order of size from top to bottom (i.e., each disk sits on 
# top of an even larger one). You have the following constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto the next tower.
# (3) A disk can only be placed on top of a larger disk.
# Write a program to move the disks from the first tower to the last using stacks.

def hanoi(A, B, C, n=None):
	""" hanoi(A, B, C, n) refers to the step that, n towers move from A to B via C
	>>> A = [0]
	>>> B = []
	>>> C = []
	>>> hanoi(A, B, C)
	>>> A
	[]
	>>> B
	[0]
	>>> C
	[]
	>>> A = [5, 4, 3, 2, 1, 0]
	>>> B = []
	>>> C = []
	>>> hanoi(A, B, C)
	>>> A
	[]
	>>> B
	[5, 4, 3, 2, 1, 0]
	>>> C
	[]
	"""
	if n is None:
		n = len(A)
	if n == 1:
		disk = A.pop()
		B.append(disk)
		return
	hanoi(A, C, B, n-1)
	hanoi(A, B, C, 1)
	hanoi(C, B, A, n-1)

if __name__ == "__main__":
	import doctest
	doctest.testmod()