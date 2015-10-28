# 6.7 The Apocalypse: In the new post-apocalyptic world, the world queen is desperately
# concerned about the birth rate. Therefore, she decrees that all families should ensure
# that they have one girl or else they face massive fines. If all families abide by this
# policy -- that is, they have continued to have children until they have one girl, at
# which point they immediately stop -- what will the gender ratio of the new generation
# be? (Assume that the odds of someone having a boy or a girl on any given pregnancy is
# equal.) Solve this out logically and then write a computer simulation of it.

import random

def simulate_birth(families):
	"""
	From the result of simulation, it seems that it doesn't really change the ratio
	of birth rate.
	Let's prove it mathematically:
	Assume the probability of giving birth to a girl/boy is p = 0.5. We have these cases:
	0 boys, 1 girl => p
	1 boy, 1 girl => p^2
	2 boys, 1 girl => p^3
	3 boys, 1 girl => p^4
	...
	The numbers after the arrows are the corresponding probabilities of that case
	It is obvious that the expectation of girls is 1 for each family, what about the
	expectation of boys?
	0 * p + 1 * p^2 + 2 * p^3 + 3 * p^4 + ... = (p/(1-p))^2 = 1
	Then the expectation of girls is equal to the expectation of boys!

	Although the intuition may tell you the policy favors girls, but notice that there are
	a lot of families who have many boys just get that one single girl, just kind of balancing
	everything out.
	>>> simulate_birth(1000)
	"""
	girls = 0
	boys = 0
	for i in range(families):
		no_girl = True
		while no_girl:
			if random.randint(0, 1) == 0:
				girls += 1
				no_girl = False
			else:
				boys += 1

	return girls, boys

"""
if __name__ == "__main__":
	import doctest
	doctest.testmod()
"""