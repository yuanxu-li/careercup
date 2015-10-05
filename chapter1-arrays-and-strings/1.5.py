# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

def is_one_away(string1, string2):
	""" Check if two strings are one edit away
	>>> is_one_away("pale", "ple")
	True
	>>> is_one_away("pales", "pale")
	True
	>>> is_one_away("pale", "bale")
	True
	>>> is_one_away("pale", "bake")
	False
	"""
	if len(string1) == len(string2):
		diff_num = 0
		for i in range(len(string1)):
			if string1[i] != string2[i]:
				diff_num += 1
				if diff_num >= 2:
					return False
		return True
	elif len(string1) + 1 == len(string2):
		diff_num = 0
		j = 0
		for i in range(len(string1)):
			if string1[i] != string2[j]:
				diff_num += 1
				if diff_num >= 2:
					return False
				j += 1
			j += 1
		return True
	elif len(string1) == len(string2) + 1:
		diff_num = 0
		j = 0
		for i in range(len(string2)):
			if string2[i] != string1[j]:
				diff_num += 1
				if diff_num >= 2:
					return False
				j += 1
			j += 1
		return True
	else:
		return False

def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()