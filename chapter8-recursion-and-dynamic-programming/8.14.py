# 8.14 Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true),
# & (AND), | (OR), and ^ (XOR), and a desired boolean result value result, implement a function
# to count the number of ways of parenthesizing the expression such that it evaluates to result.

def count_eval(expr, result, memo={True: {}, False: {}}):
	"""
	>>> count_eval("1^0|0|1", False)
	2
	>>> count_eval("0&0&0&1^1|0", True)
	10
	"""
	# return calculated result
	if expr in memo[result]:
		return memo[result][expr]

	# recursive case
	count = 0
	for i in range(len(expr)):
		if expr[i] == "&":
			if result is True:
				count += count_eval(expr[:i], True, memo) * count_eval(expr[i+1:], True, memo)
			else:
				count += count_eval(expr[:i], False, memo) * count_eval(expr[i+1:], False, memo) \
					   + count_eval(expr[:i], False, memo) * count_eval(expr[i+1:], True, memo) \
					   + count_eval(expr[:i], True, memo) * count_eval(expr[i+1:], False, memo)
		elif expr[i] == "|":
			if result is True:
				count += count_eval(expr[:i], True, memo) * count_eval(expr[i+1:], True, memo) \
					   + count_eval(expr[:i], False, memo) * count_eval(expr[i+1:], True, memo) \
					   + count_eval(expr[:i], True, memo) * count_eval(expr[i+1:], False, memo)
			else:
				count += count_eval(expr[:i], False, memo) * count_eval(expr[i+1:], False, memo)
		elif expr[i] == "^":
			if result is True:
				count += count_eval(expr[:i], False, memo) * count_eval(expr[i+1:], True, memo) \
					   + count_eval(expr[:i], True, memo) * count_eval(expr[i+1:], False, memo)
			else:
				count += count_eval(expr[:i], False, memo) * count_eval(expr[i+1:], False, memo) \
				       + count_eval(expr[:i], True, memo) * count_eval(expr[i+1:], True, memo)
	# if count is larger than one, then it is recursive case
	if count > 0:
		return count
	else:
		# base case
		if result is True and expr == "1" or result is False and expr == "0":
			memo[result][expr] = 1
			return 1
		else:
			memo[result][expr] = 0
			return 0

if __name__ == "__main__":
	import doctest
	doctest.testmod()