# 5.5 Debugger: Explain what the following code does: ((n & (n - 1)) == 0)

def debugger(n):
	"""
	Check if n is the power of 2(or 0). For example, 16 is 1000 in binary base, and 16-1 is 0111 in binary base.
	It is easy to see that, only in this case (n being the power of 2), that n & (n-1) will be 0
	>>> debugger(1)
	True
	>>> debugger(16)
	True
	>>> debugger(1024)
	True
	>>> debugger(4096)
	True
	>>> debugger(4025)
	False
	"""
	return (n & (n - 1)) == 0

if __name__ == "__main__":
	import doctest
	doctest.testmod()