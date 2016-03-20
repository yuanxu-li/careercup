# 10.8 Find Duplicates: You have an array with all the numbers from 1 to N.
# where N is at most 32,000. The array may have duplicate entries and you do
# not know what N is. With only 4 kilobytes of memory available, how would you
# print all duplicate elements in the array?

# We can create a bit vector with 32,000 bits, where each bit represents one integer.
# Using this bit vector, we can then iterate through the array, flagging each element v
# by setting bit v to 1. When we come across a duplicate element, we print it.