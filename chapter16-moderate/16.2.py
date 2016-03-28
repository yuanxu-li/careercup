# 16.2 Word Frequencies: Design a method to find the frequency of occurences of
# any given word in a book. What if we were running this algorithm multiple times?

class Book:
	def __init__(self, content):
		"""
		both the content as string and content_list as list, which is a list of all words, are stored
		"""
		self.search_list = {}
		if content is None:
			self.content = ""
			self.content_list
		else:
			self.content = content
			self.content_list = [word.strip("\"',?!./\\") for word in content.split()]

	def find_frequency(self, word):
		"""
		>>> book = Book("The most mysterious season of Game of Thrones yet is also the best — that’s according to the HBO drama’s Emmy-winning showrunners David Benioff and Dan Weiss. Normally the writer-producers are pretty cautious about making statements that raise fans’ already astronomic expectations for their international hit series. But they recently watched the near-final cuts of all 10 episodes, and we asked which aspect was the most exciting.")
		>>> book.find_frequency("most")
		2
		"""
		if word not in self.search_list:
			self.search_list[word] = self.content_list.count(word)
		return self.search_list[word]

if __name__ == "__main__":
	import doctest
	doctest.testmod()