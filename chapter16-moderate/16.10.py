# 16.10 Living People: Given a list of people with their birth and death years, implement
# a method to compute the year with the most number of people alive. You may assume that
# all people were born between 1900 and 2000 (inclusive). If a person was alive during any
# portion of that year, they should be included in that year's count. For example, Person
# (birth = 1908, death = 1909) is included in the counts for both 1908 and 1909.

from collections import defaultdict

people = [
	["1902", "1903"],
	["1905", "1940"],
	["1930", "1999"],
	["1999", "2000"],
	["1979", "1998"],
	["1901", "1930"],
	["1940", "1940"],
	["1940", "1940"],
	["1940", "1940"],
	["1940", "1940"],
	["1940", "1940"],
	["1940", "1940"],
	["1940", "1940"],
	["1940", "1940"],
	["1940", "1940"],
	["1940", "1940"]
]

def year_most_people_alive(people):
	"""
	>>> year_most_people_alive(people)
	'1940'
	"""
	d = defaultdict(int)
	for i in range(len(people)):
		d[people[i][0]] += 1
	return max(d, key=lambda k: d[k])



if __name__ == "__main__":
	import doctest
	doctest.testmod()