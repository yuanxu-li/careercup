# 8.1 Triple steps: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

def triple_step_memoized(n, memo=None):
	""" To reach one stair, we need to consider what the previous stair is. Since the child can hop either 1 step, 2 steps, or 3 steps.
	The previous stair could be either n-1, n-2, or n-3. Since they are exclusive, the number of ways to reach stair n is decided by
	the sum of the number of ways to reach n-1, n-2 and n-3. However, to avoid recalculation for some stairs, memoization is employed.
	>>> triple_step_memoized(1)
	1
	>>> triple_step_memoized(2)
	2
	>>> triple_step_memoized(3)
	4
	>>> triple_step_memoized(4)
	7
	"""
	if memo is None:
		return triple_step_memoized(n, {})

	# base case
	if n < 0:
		return 0
	elif n == 0:
		return 1
	# memoized
	elif n in memo:
		return memo[n]
	# new
	else:
		memo[n] = triple_step_memoized(n-1, memo) + triple_step_memoized(n-2, memo) + triple_step_memoized(n-3, memo)
		return memo[n]

def triple_step_simplified(n):
	""" Notice that to compute the number of ways to reach one stair, we just need the number of ways for three previous stairs.
	Then each step we only store the number of ways for three previous stairs using three variables.
	>>> triple_step_simplified(1)
	1
	>>> triple_step_simplified(2)
	2
	>>> triple_step_simplified(3)
	4
	>>> triple_step_simplified(4)
	7
	"""
	a = 0
	b = 0
	c = 1
	for i in range(n):
		temp = a + b + c
		a, b, c = b, c, temp
	return temp



if __name__ == "__main__":
	import doctest
	doctest.testmod()