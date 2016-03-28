# 16.20 T9: On old cell phones, users typed on a numeric keypad and the phone would
# provide a list of words that matched these numbers. Each digit mapped to a set
# of 0-4 letters. Implement an algorithm to return a list of matching words, given
# a sequence of digits. You are provided a list of valid words (provided in whatever
# data structure you'd like). The mapping is shown in the diagram below:
# EXAMPLE
# Input: 8733
# Output: tree, used

class Node:
	mapping = {
		"2": "abc",
		"3": "def",
		"4": "ghi",
		"5": "jkl",
		"6": "mno",
		"7": "pqrs",
		"8": "tuv",
		"9": "wxyz"
	}
	def __init__(self, letter):
		self.letter = letter
		self.children = []

	def append_child(self, child):
		self.children.append(child)

	def find_child(self, letter):
		for child in self.children:
			if child.letter == letter:
				return child
		return None



def build_word_tree(words):
	"""
	We are building a word tree based on a list of words.
	The tree structure is like, each node represents a letter, and its children represents
	all possible letters that can follow it. For example, "tree" will be "t" node, and its
	child "r" node and its child "e" node and its child "e" node.
	To make all in one tree, we have an empty root node, so that the first letters of every word
	will be its direct children.
	"""
	root = Node("")
	for word in words:
		cur = root
		for l in word:
			prev = cur
			cur = prev.find_child(l)
			if cur is None:
				cur = Node(l)
				prev.children.append(cur)
		cur.children.append(Node(""))
	return root

def search_word_tree(root, number, prefix=None):
	"""
	We always try to compare the children of the root with the current number
	>>> root = build_word_tree(["tree", "used", "try", "unusual", "friend", "alias"])
	>>> list(search_word_tree(root, "8733"))
	['tree', 'used']
	"""
	# alternative for initial call
	if prefix is None:
		prefix = ""
		for child in root.children:
			yield from search_word_tree(child, number, "")
		return

	# reach the leaf node
	if not root.letter:
		# the number has been run out
		if not number:
			yield prefix
		return

	# number has been run out
	if not number:
		return

	# compare the first number with the current node
	if root.letter in root.mapping[number[0]]:
		for child in root.children:
			yield from search_word_tree(child, number[1:], prefix + root.letter)


if __name__ == "__main__":
	import doctest
	doctest.testmod()










