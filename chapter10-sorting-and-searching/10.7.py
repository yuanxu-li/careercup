# 10.7 Missing Int: Given an input file with four billion non-negative integers,
# provide an algorithm to generate an integer that is not contained in the file.
# Assume you have 1 GB of memory available for this task.

"""
We can map all integers into bits of a series of bytes, and find the first
non-zero bit along the bytes
"""