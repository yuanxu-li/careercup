# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other

def check_permutation(string1, string2):
	"""transform the two strings into dict(hash table), and compare if the two dicts are the same
	>>> check_permutation("asdf", "fdsa")
	True
	>>> check_permutation("asdf", "asdff")
	False
	>>> check_permutation("", "")
	True
	"""
	dict1 = {}
	for char in string1:
		if char in dict1:
			dict1[char] += 1
		else:
			dict1[char] = 0

	dict2 = {}
	for char in string2:
		if char in dict2:
			dict2[char] += 1
		else:
			dict2[char] = 0

	return dict1 == dict2

def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()