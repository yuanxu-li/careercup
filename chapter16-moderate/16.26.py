# 16.26 Calculator: Given an arithmetic equation consisting of positive integers,
# +, -, * and / (no parentheses), compute the result.
# EXAMPLE
# Input: 2*3+5/6*3+15
# Output: 23.5

def evaluate_add_item(s):
	"""
	>>> evaluate_add_item("2*3+5/6*3+15")
	23.5
	"""
	operator = None
	for i in range(len(s)):
		if s[i] == "+" or s[i] == "-":
			operator = s[i]
			break

	if operator == "+":
		return evaluate_multiply_item(s[0:i]) + evaluate_add_item(s[i+1:])
	elif operator == "-":
		return evaluate_multiply_item(s[0:i]) - evaluate_add_item(s[i+1:])
	else:
		return evaluate_multiply_item(s)

def evaluate_multiply_item(s):
	operator = None
	for i in range(len(s)-1, -1, -1):
		if s[i] == "*" or s[i] == "/":
			operator = s[i]
			break

	if operator == "*":
		return evaluate_multiply_item(s[0:i]) * evaluate_integer_item(s[i+1:])
	elif operator == "/":
		return evaluate_multiply_item(s[0:i]) / evaluate_integer_item(s[i+1:])
	else:
		return evaluate_integer_item(s)

def evaluate_integer_item(s):
	result = 0
	for i in range(len(s)):
		digit = int(s[i])
		result = result * 10 + digit
	return result

if __name__ == "__main__":
	import doctest
	doctest.testmod()