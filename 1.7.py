# 1.7 Rotate Matrix: Given an image represented by an N*N matrix, where each pixel in the image is 4 bytes, write a method to rotate
# the image by 90 degrees. Can you do this in place?

def rotate_matrix(matrix):
	""" Take a matrix (list of lists), and rotate the matrix clockwise
	>>> rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])
	[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
	>>> rotate_matrix([])
	[]
	"""
	length = len(matrix)

	# first, flip along the main diagonal
	for i in range(length):
		for j in range(i+1, length):
			# swap two elements
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	# second, flip left and right
	for i in range(length):
		for j in range(int(length/2)):
			# swap two elements
			matrix[i][j], matrix[i][length-1-j] = matrix[i][length-1-j], matrix[i][j]

	return matrix

def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()