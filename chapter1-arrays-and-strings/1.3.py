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
	space_count = 0
	for i in range(0, length):
		if string_list[i] == " ":
			space_count += 1
	new_length = length + space_count * 2
	for i in range(length - 1, -1, -1):
		if string_list[i] == " ":
			string_list[new_length - 1] = "0"
			string_list[new_length - 2] = "2"
			string_list[new_length - 3] = "%"
			new_length -= 3
		else:
			string_list[new_length - 1] = string_list[i]
			new_length -= 1

	return "".join(string_list).strip()

def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()