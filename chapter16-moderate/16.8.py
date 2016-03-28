# 16.8 English int: Given any integer, print an English phrase that describes the integer
# (e.g., "One Thousand, Two Hundred Thirty Four").

import pdb

unit_map = { \
	1: "One", \
	2: "Two", \
	3: "Three", \
	4: "Four", \
	5: "Five", \
	6: "Six", \
	7: "Seven", \
	8: "Eight", \
	9: "Nine", \
}

ten_unit_map = { \
	2: "Twenty", \
	3: "Thirty", \
	4: "Forty", \
	5: "Fifty", \
	6: "Sixty", \
	7: "Seventy", \
	8: "Eighty", \
	9: "Ninety", \
	10: "Ten", \
	11: "Eleven", \
	12: "Twelve", \
	13: "Thirteen", \
	14: "Fourteen", \
	15: "Fifteen", \
	16: "Sixteen", \
	17: "Seventeen", \
	18: "Eighteen", \
	19: "Nineteen" \
}

thousand_unit_map = { \
	0: "", \
	1: " Thousand", \
	2: " Million", \
	3: " Billion", \
	4: " Trillion" \
}

def english_int(n):
	"""
	>>> english_int(12345)
	'Twelve Thousand, Three Hundred Forty Five'
	>>> english_int(1242359034)
	'One Billion, Two Hundred Forty Two Million, Three Hundred Fifty Nine Thousand, Thirty Four'
	>>> english_int(0)
	''
	"""
	# arr stores all the thousand result
	arr = []
	index = 0
	while n > 0:
		thousand_part = n % 1000
		result = thousand_english_int(thousand_part, index)
		if len(result) > 0:
			arr.append(result)
		index += 1
		n = n // 1000

	return ", ".join(reversed(arr))


def thousand_english_int(n, index):
	""" deal with an int less than 1,000
	"""
	hundred = n // 100
	ten = (n - 100 * hundred) // 10
	unit = (n - 100 * hundred) % 10
	result = []

	# pdb.set_trace()

	# has hundred
	if hundred > 0:
		result.append(unit_map[hundred] + " Hundred")

	# has ten
	if ten > 0:
		if ten == 1:
			result.append(ten_unit_map[ten * 10 + unit])
		else:
			result.append(ten_unit_map[ten])
			if unit > 0:
				result.append(unit_map[unit])
	# does not have ten
	else:
		if unit > 0:
			result.append(unit_map[unit])

	if len(result) > 0:
		return " ".join(result) + thousand_unit_map[index]
	else:
		return ""



if __name__ == "__main__":
	import doctest
	doctest.testmod()