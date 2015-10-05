# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letter.
# The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True(permutations: "taco cat", "atco cta", etc.)

def is_palindrome_permutation(string):
	"""to be a permutation of a palindrome, a string must have odd occurrence for less than one character, and even occurrences for other characters
	>>> is_palindrome_permutation("Tact Coa")
	True
	>>> is_palindrome_permutation("Tact Coaa")
	False
	>>> is_palindrome_permutation("")
	True
	"""
	# lower the case and remove whitespaces from the string
	clean_string = "".join(string.lower().split())
	palindrome_dict = {}
	for char in clean_string:
		if char in palindrome_dict:
			palindrome_dict[char] += 1
		else:
			palindrome_dict[char] = 1

	odd_occurrences = 0
	even_occurrences = 0
	for char in palindrome_dict:
		if palindrome_dict[char] % 2 == 0:
			even_occurrences += 1
		else:
			odd_occurrences += 1

	if odd_occurrences <= 1:
		return True
	else:
		return False

def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()