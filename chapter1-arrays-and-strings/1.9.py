# 1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
# (e.g., "waterbottle" is a rotation of "erbottlewat")

def is_substring(substring, string):
	return substring in string

def is_string_rotation(s1, s2):
	""" Check if s2 is a rotation of s1 with only one call to is_substring
	>>> is_string_rotation("waterbottle", "erbottlewat")
	True
	>>> is_string_rotation("waterbottle", "terbottlewa")
	True
	>>> is_string_rotation("waterbottle", "terbottlewk")
	False
	>>> is_string_rotation("wat", "aatw")
	False
	>>> is_string_rotation("", "")
	True
	"""
	if len(s1) != len(s2):
		return False
	return is_substring(s2, s1 + s1)

def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()