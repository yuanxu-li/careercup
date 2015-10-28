# 6.4 Ants on a Triangle: There are three ants on different vertices of a triangle.
# What is the probability of collision (between any two or all of them) if they
# start walking on the sides of the triangle? Assume that each ant randomly picks
# a direction, with either direction being equally likely to be chosen, and that
# they walk at the same speed.
# Similarly, find the probability of collision with n ants on an n-vertex polygon.

# When we have n ants on n-vertex polygon, we have 2^n arrangements for each ant has
# 2 directions to choose from. However, only 2 arrangements will not lead to collision,
# clockwise and anti-clockwise. Then the probability is:
# p = 2 / 2^n = 2^(1-n)