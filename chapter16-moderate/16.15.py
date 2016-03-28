# 16.15 Master Mind: The Game of Master Mind is played as follows:
# The computer has four slots, and each slot will contain a ball that is red(R), yellow(Y),
# green(G) or blue(B). For example, the computer might have RGGB(Slot #1 is red, Slots #2 and #3
# are green, Slot #4 is blue)
# You, the user, are trying to guess the solution. You might, for example, guess YRGB.
# When you guess the correct color for the correct solot, you get a "hit". If you guess a color
# that exists but is in the wrong slot, you get a "pseudo-hit". Note that a slot that is a hit
# can never count as a pseudo-hit.
# For example, if the actual solution is RGBY and you guess GGRR, you have one hit and one
# pseudo-hit.
# Write a method that, given a guess and a solution, returns the number of hits and pseudo-hits.

from collections import defaultdict

def master_mind(guess, solution):
	"""
	>>> master_mind(["red", "green", "black", "yellow"], ["green", "green", "red", "red"])
	(1, 1)
	"""
	hits = 0
	pseudo_hits = 0
	guess_dict = defaultdict(int)
	solution_dict = defaultdict(int)


	# O(n), counting hits, and store all unmatched colors into two dictionaries
	for i in range(len(guess)):
		if solution[i] == guess[i]:
			hits += 1
		else:
			guess_dict[guess[i]] += 1
			solution_dict[solution[i]] += 1

	# since all matched slots have been counted as hits and are not stored in the dictionaries,
	# we simply compare the number of colors in two dictionaries, and decide the smaller number
	# is the pseudo-hit for that color
	for color in solution_dict:
		if solution_dict[color] > guess_dict[color]:
			pseudo_hits += guess_dict[color]
		else:
			pseudo_hits += solution_dict[color]

	return hits, pseudo_hits

if __name__ == "__main__":
	import doctest
	doctest.testmod()
