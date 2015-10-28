# 6.2 Basketball: You have a basketball hoop and someone says that you can play one
# of two games.
# Game 1: You get one shot to make the hoop.
# Game 2: You get three shots and you have to make two of three shots.
# If p is the probability of making a particular shot, for which values of p
# should you pick one game or the other?

# p1 = p
# p2 = 3 * p^2 * (1-p) + p^3
# 	 = 3 * p^2 - 2 * p^3

# When we choose game 1 over game 2, p1 > p2, which leads to:
# => p > 3 * p^2 - 2 * p^3
# since 0 < p < 1,
# => 0 < p < 0.5

# Similarly, when we choose game 2 over game1, we shall have 0.5 < p < 1,
# and when we choose either game, we shall have p = 0.5