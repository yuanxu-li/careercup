# 5.8 Draw Line: A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels
# to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will be split
# across rows). The height of the screen, of course, can be derived from the length of the array and the width.
# Implement a function that draws a horizontal line from (x1, y) to (x2, y).
# The method signature should look something like:
# drawLine(byte[] screen, int width, int x1, int x2, int y)

import pdb

def draw_line(screen, width, x1, x2, y):
	""" find the indices of x1 and x2, fix the bytes of x1 and x2 and in between.
	>>> screen = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	>>> draw_line(screen, 24, 4, 22, 1)
	>>> screen[3]
	15
	>>> screen[4]
	255
	>>> screen[5]
	254
	"""
	if width % 8 != 0:
		raise Exception("width is not multiple of 8!")
	x1_ind = y * (width // 8) + x1 // 8
	x1_offset = x1 % 8
	x2_ind = y * (width // 8) + x2 // 8
	x2_offset = x2 % 8



	# fix the bytes between x1 and x2
	for ind in range(x1_ind + 1, x2_ind):
		screen[ind] = 255

	# if x1 and x2 are in different bytes
	if x1_ind != x2_ind:
		# fix the byte of x1
		mask = (1 << (8 - x1_offset)) - 1
		screen[x1_ind] |= mask
		# fix the byte of x2
		mask = (1 << (x2_offset + 1)) - 1
		mask <<= (8 - x2_offset - 1)
		screen[x2_ind] |= mask
	# if x1 and x2 are in the same byte
	else:
		mask1 = (1 << (8 - x1_offset)) - 1
		mask2 = (1 << (x2_offset + 1)) - 1
		mask2 <<= (8 - x2_offset - 1)
		screen[x1_ind] |= (mask1 & mask2)


if __name__ == "__main__":
	import doctest
	doctest.testmod()