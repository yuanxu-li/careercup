# 8.12 Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8*8 chess board
# so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all diagonals,
# not just the two that bisect the board.

import pdb

def arrange_queen(board, row=0):
	"""
	>>> len(list(arrange_queen([[0 for i in range(8)] for j in range(8)])))
	92
	"""
	# print(row)
	if row >= len(board):
		# yield a deep copy of board
		yield [line[:] for line in board]

	for col in range(len(board)):
		# print((row, col))
		if valid_position(board, row, col):
			
			board[row][col] = 1
			yield from arrange_queen(board, row+1)
			board[row][col] = 0

def valid_position(board, row, col):
	# search through the same column
	# print("valid_position " + str(row) + " " + str(col))
	for i in range(row):
		if board[i][col]: 
			return False
	# search through upper-left diagonal
	i, j = row, col
	while i >= 0 and j >= 0:
		if board[i][j]:
			return False
		i -= 1
		j -= 1

	# search through upper-right diagonal
	i, j = row, col
	while i >= 0 and j < len(board):
		if board[i][j]:
			return False
		i -= 1
		j += 1
	# if pass all the tests, return True
	return True

if __name__ == "__main__":
	import doctest
	doctest.testmod()


