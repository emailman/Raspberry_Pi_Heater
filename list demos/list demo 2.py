from random import shuffle

# Generate a list of numbers from 1 to 5
s = list(range(1, 6))

# Shuffle the list
shuffle(s)

# Print the list
print(s)

# Print and pop each item from the list
# until it is empty
while len(s) != 0:
    print(s.pop(0))
