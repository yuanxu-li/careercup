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
	i = 0
	j = 0
	while j < len(s2):
		# if the two characters are the same, then move both i and j one step forward
		if s2[j] == s1[i]:
			i += 1
			j += 1
		# if the two characters are not the same
		else:
			i = 0
			# if miss the first character, move j one step forward, otherwise keep j at the same place, for it is possible to match the first character
			if i == 0:
				j += 1

	return is_substring(s1[i:], s2[:-i])

def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()