# 6.6 Blue-Eyed Island: A bunch of people are living on an island, when a visitor
# comes with a strange order: all blue-eyed people must leave the island as soon
# as possible. There will be a flight out at 8:00 pm every evening. each person
# can see everyone else's eye color, but they do not know their own (nor is anyone
# allowed to tell them). Additionally, they do not know how many people have blue eyes,
# although they do know that at least one person does. How many days will it take
# the blue-eyed people to leave?

# Let's see the case of different numbers of blue-eyes people

# 1 blue-eyed person

# day 1: I see nobody else is blue-eyed, and the precondition is there is at least
# one who is blue-eyed. It has to be me, let's fly~

# 2 blue-eyed persons

# day 1: I see one blue-eyed person, if he is the only blue-eyed person, he is going
# to leave tonight.

# day 2: What? He didn't leave yesterday? I see, I am blue-eyed, too, and he is thinking
# the same as me

# 3 blue-eyed persons
# I see two blue-eyed persons, if I am not blue-eyed, it shall take them two days to
# figure it out and leave.
# day 3: What? They haven't left? I see, I am blue-eyed too. Let's leave together tonight

# The pattern is obvious, it takes n blue-eyed persons n days to figure everything out.