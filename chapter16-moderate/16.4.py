# 16.4 Tic Tac Win: Design an algorithm to figure out if someone has won a game
# of tic-tac-toe

def validate_win(board, player):
	"""
	>>> validate_win([[None, None, 1], [None, 0, 0], [1, 1, 1]], 1)
	True
	>>> validate_win([[None, None, 1], [None, 0, 0], [1, 1, 1]], 0)
	False
	"""

	n = len(board)
	rows = [True for i in range(n)]
	columns = [True for i in range(n)]

	
	# check two diagonals
	for i in range(n):
		if board[i][i] != player:
			rows[i] = False
			columns[i] = False
			break
	if i == n:
		return True

	for i in range(n):
		if board[i][n-1-i] != player:
			rows[i] = False
			columns[n-1-i] = False
			break
	if i == n:
		return True

	# loop through all the elements in the board, set the mark for correspoinding rows
	# and columns to false if this element does not belong to the player
	for i in range(n):
		for j in range(n):
			if board[i][j] != player:
				rows[i] = False
				columns[j] = False

	return True in rows or True in columns

if __name__ == "__main__":
	import doctest
	doctest.testmod()