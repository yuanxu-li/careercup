# 1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space
# at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing
# in Java, please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith      ", 13
# Output: "Mr%20John%20Smith"

def URLify(string_list, length):
	"""Take in a string list and a given length of the true string, and replace spaces with '%20' using in-place approach
	>>> URLify(list("Mr John Smith                                     "), 13)
	'Mr%20John%20Smith'
	"""
	j = length
	for i in range(0, length):
		if string_list[i] == " ":
			string_list[j] = "%"
			j += 1
			string_list[j] = "2"
			j += 1
			string_list[j] = "0"
			j += 1
		else:
			string_list[j] = string_list[i]
			j += 1

	return ''.join(string_list[length:j])

def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()