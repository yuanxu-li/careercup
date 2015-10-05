# 1.6 String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the
# original string, your method should return the original string. You can assume the string has only uppercase and lowercase
# letters (a-z).

def string_compression(string):
	""" compress a string using the counts of repeated characters
	>>> string_compression("aabcccccaaa")
	'a2b1c5a3'
	>>> string_compression("abcdefg")
	'abcdefg'
	>>> string_compression("")
	''
	"""
	# compressed_string_list stores char and counts right after each char
	compressed_string_list = []
	for char in string:
		# initilize the first char in compressed_string_list
		if len(compressed_string_list) == 0 or char != compressed_string_list[-2]:
			compressed_string_list.extend([char, 1])
		elif char == compressed_string_list[-2]:
			compressed_string_list[len(compressed_string_list)-1] += 1

	if len(compressed_string_list) >= len(string):
		return string
	else:
		return "".join([str(instance) if type(instance) is int else instance for instance in compressed_string_list])

def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()