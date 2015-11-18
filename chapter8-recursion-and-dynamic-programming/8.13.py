# 8.13 Stack of Boxes: You have a stack of n boxes, with width wi, heights hi, and depths di.
# The boxes cannot be rotated and can only be stacked on top of one another if each box in
# the stack is strictly larger than the box above it in width, height, and depth. Implement
# a method to compute the height of the tallest possible stack. The height of a stack is the
# sum of the heights of each box.

def calc_box_order(boxes):
	result = []
	for box in boxes:
		above_boxes = []
		for i in range(len(boxes)):
			box_other = boxes[i]
			if box_other[0] < box[0] and box_other[1] < box[1] and box_other[2] < box[2]:
				above_boxes.append(i)
		result.append(above_boxes)
	return result


def calc_height_tallest_stack(boxes):
	"""
	>>> boxes = []
	>>> boxes.append([4, 5, 3])
	>>> boxes.append([7, 2, 5])
	>>> boxes.append([4, 5, 2])
	>>> boxes.append([2, 4, 7])
	>>> boxes.append([5, 8, 5])
	>>> boxes.append([4, 8, 5])
	>>> boxes.append([9, 9, 9])
	>>> calc_height_tallest_stack(boxes)
	"""
	box_order = calc_box_order(boxes)
	memo = {}
	return max([height_tallest_stack(boxes, box_index, box_order, memo) for box_index in range(len(boxes))])

			

def height_tallest_stack(boxes, box_index, box_order, memo):

	# if the largest height of stack based on the box has been calculated
	if box_index in memo:
		return memo[box_index]
	# if not other boxes can be put on top of this one, return its height
	if not box_order[box_index]:
		memo[box_index] = boxes[box_index][1]
		return boxes[box_index][1]
	else:
		largest_height = boxes[box_index][1]+ max([height_tallest_stack(boxes, avail_box_index, box_order, memo) for avail_box_index in box_order[box_index]])
		memo[box_index] = largest_height
		return largest_height

if __name__ == "__main__":
	import doctest
	doctest.testmod()