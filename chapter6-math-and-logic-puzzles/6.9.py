# 6.9 100 Lockers: There are 100 closed lockers in a hallway. A man begins by opening all 100 lockers.
# Next, he closes every second locker. Then, on his third pass, he toggles every third locker (closes
# it if it is open or opens it if it is closed). This process continues for 100 passes, such that on
# each pass i, the man toggles every ith locker. After his 100th pass in the hallway, in which he toggles
# only locker #100, how many lockers are open?

def open_lockers(n):
	"""
	closed denoted by 0, while open denoted by 1
	>>> open_lockers(100)
	10
	"""
	lockers = [0 for i in range(n)]
	for i in range(0, n):
		for j in range(i, n, i+1):
			lockers[j] = abs(lockers[j] - 1)
	return sum(lockers)

if __name__ == "__main__":
	import doctest
	doctest.testmod()