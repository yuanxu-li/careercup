# 6.2 Basketball: You have a basketball hoop and someone says that you can play one
# of two games.
# Game 1: You get one shot to make the hoop.
# Game 2: You get three shots and you have to make two of three shots.
# If p is the probability of making a particular shot, for which values of p
# should you pick one game or the other?

# p1 = p
# p2 = 3 * p^2 * (1-p) + p^3
# 	 = p^2 * (3-p)

# When we choose game 1 over game 2, p1 > p2, which leads to:
# => p > p^2 * (3-p)
# since 0 < p < 1,
# => p < (3+sqrt(5))/2

# Similarly, when we choose game 2 over game1, we shall have p < (3+sqrt(5))/2,
# and when we choose either game, we shall have p = (3+sqrt(5))/2