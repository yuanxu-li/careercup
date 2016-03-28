# 16.18 Pattern Matching: You are given two strings, pattern and value. The pattern
# string consists of just the letters a and b, describing a pattern within a string.
# For example, the string catcatgocatgo matches the pattern aabab (where cat is a a
# and go is b). It also matches patterns like a, ab, and b. Write a method to
# determine if value matches pattern.

import pdb

def pattern_match(pattern, value):
	""" Given a pattern and a value, we need to try different lengths of a and b,
	only after we have exhausted all possible lengths for a and b, can we say they do
	not match
	>>> pattern_match("aabab", "catcatgocatgo")
	True
	>>> pattern_match("a", "catcatgocatgo")
	True
	>>> pattern_match("b", "catcatgocatgo")
	True
	>>> pattern_match("ab", "catcatgocatgo")
	True
	"""
	# edge case
	if not value or not pattern:
		return False

	count_a = pattern.count("a")
	count_b = pattern.count("b")

	# no a and no b in pattern
	if count_a == 0 and count_b == 0:
		return False
	# only b in pattern
	elif count_a == 0 and count_b != 0:
		if len(value) % count_b != 0:
			return False
		else:
			len_b = len(value) // count_b
			b = value[0:len_b]
			for i in range(1, len(pattern)):
				if value[i*len_b : (i+1)*len_b] != b:
					return False
			return True
	# only a in pattern
	elif count_a != 0 and count_b == 0:
		if len(value) % count_a != 0:
			return False
		else:
			len_a = len(value) // count_a
			a = value[0:len_a]
			for i in range(1, len(pattern)):
				if value[i*len_a : (i+1)*len_a] != a:
					return False
			return True
	# both a and b in pattern
	else:
		len_a = 1
		# try different pairs of a and b's lengths
		# pdb.set_trace()
		while len_a * count_a < len(value):
			if (len(value) - len_a * count_a) % count_b == 0:
				# now start trying to apply this pattern to value with the given pair of a and 
				# b's lengths
				len_b = (len(value) - len_a * count_a) // count_b
				# loop through pattern to match value
				a = ""
				b = ""
				i = 0 # index for pattern
				j = 0 # index for value
				while i < len(pattern):
					# compare a
					if pattern[i] == "a":
						# store the first a, and store it as comparison baseline
						if not a:
							a = value[j : j+len_a]
						else:
							if value[j : j+len_a] != a:
								break
						j += len_a

					elif pattern[i] == "b":
						if not b:
							b = value[j : j+len_b]
						else:
							if value[j : j+len_b] != b:
								break
						j += len_b
					else:
						# pattern should not allow any other characters except a and b
						return False
					i += 1
				# if we succeed in finishing the matching process
				if i == len(pattern):
					return True
			len_a += 1

	return False


if __name__ == "__main__":
	import doctest
	doctest.testmod()