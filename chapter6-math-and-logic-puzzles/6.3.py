# 6.3 Dominos: There is an 8*8 chessboard in which two diagonally opposite corners
# have been cut off. You are given 31 dominos, and a single domino can cover
# exactly two squares. Can you use the 31 dominos to cover the entire board?
# Prove your answer (by providing an example or showing why it's impossible).

# We have 62 squares to be covered and 31 dominos to cover, and thus we need
# each domino to cover two squares and there is no overlap.
# Notice that A domino can cover only one white square and one black square.
# However, two diagonally opposite corners are either both white or both black.
# Let's, they are both black. Then we have 32 black squares to cover and 30 white
# squares to cover, which is impossible for 31 dominos.