# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def is_unique_1(string):
	"""use dict(hash table), O(n) time but need extra data structure
	>>> is_unique_1("asdfghjklas")
	False
	>>> is_unique_1("asdf")
	True
	>>> is_unique_1("")
	True
	"""
	string_set = set();
	for char in string:
		if char in string_set:
			return False
		else:
			string_set.add(char)
	return True

def is_unique_2(string):
	""" use in-place sort O(nlogn) and find if there is any adjacent neighbors
	>>> is_unique_2("asdfghjklas")
	False
	>>> is_unique_2("asdf")
	True
	>>> is_unique_2("")
	True
	"""
	string_list = list(string)
	string_list.sort()
	for i in range(1, len(string_list)):
		if string_list[i] == string_list[i-1]:
			return False
	return True


def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()