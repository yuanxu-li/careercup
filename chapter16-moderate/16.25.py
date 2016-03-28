# 16.25 LRU Cache: Design and build a "least recently used" cache,
# which evicts the least recently used item. The cache should map
# from keys to values (allowing you to insert and retrieve a value
# associated with a particular key) and be initialized with a max size.
# When it is full, it should evict the least recently used item.

from collections import deque

class LRUCache:
	"""
	>>> cache = LRUCache(3)
	>>> cache.insert(1, "11111")
	>>> cache.insert(2, "22222")
	>>> cache.insert(3, "33333")
	>>> cache.retrieve(1)
	'11111'
	>>> cache.insert(4, "44444")
	>>> cache.retrieve(2)
	'Not found!'
	"""
	def __init__(self, max_size):
		self.max_size = max_size
		self.cache = {}
		self.timestamp = 0

	def retrieve(self, key):
		if key in self.cache:
			self.cache[key]["time"] = self.timestamp
			self.timestamp += 1
			return self.cache[key]["value"]
		else:
			return "Not found!"

	def insert(self, key, value):
		# if the key is in it already, no need to evict any item
		if key in self.cache:
			self.cache[key]["time"] = self.timestamp
			self.timestamp += 1
			self.cache[key]["value"] = value
		# if it is a new key
		else:
			# check to see if there is any space
			while len(self.cache) >= self.max_size:
				lru_key = min(self.cache, key=lambda x: self.cache[x]["time"])
				del self.cache[lru_key]

			self.cache[key] = {"time": self.timestamp, "value": value}
			self.timestamp += 1

if __name__ == "__main__":
	import doctest
	doctest.testmod()