# 11.1 Mistake: Find the mistake(s) in the following code:
unsigned int i;
for (i = 100; i >= 0; --i)
	printf("%d\n", i);

# first, unsigned int i is always larger than zero by definition, and thus the loop
# will go forever
# second, the format to print out an unsigned variable is %u, instead of %d