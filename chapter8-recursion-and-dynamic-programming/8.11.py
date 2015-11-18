# 8.11 Coins: Given an infinite number of quarters (25 centers), dimes (10 cents), nickels (5 cents),
# and pennies (1 cent), write code to calculate the number of ways of representing n cents.

def represent_cent(n, coin_array, coin_index=0):
	""" 
	>>> represent_cent(20, [25, 10, 5, 1])
	9
	"""
	# boundary case
	if n == 0:
		return 1
	elif n < 0 or coin_index >= len(coin_array):
		return 0

	num_of_ways = 0
	for i in range(coin_index, len(coin_array)):
		while n >= 0:
			num_of_ways += represent_cent(n, coin_array, coin_index + 1)
			#print((num_of_ways, n))
			n -= coin_array[coin_index]
	return num_of_ways

if __name__ == "__main__":
	import doctest
	doctest.testmod()