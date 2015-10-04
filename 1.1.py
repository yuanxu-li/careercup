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

# 
def is_unique_2(string):
	"""use no extra data structure but requires O(n^2) time
	>>> is_unique_2("asdfghjklas")
	False
	>>> is_unique_2("asdf")
	True
	>>> is_unique_2("")
	True
	"""
	for i in range(len(string)):
		cmp_char = string[i]
		for j in range(i+1, len(string)):
			if string[j] == cmp_char:
				return False
	return True

def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()