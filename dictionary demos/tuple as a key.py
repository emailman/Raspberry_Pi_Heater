import random

# Using a tuple as a key for a dictionary

# Create an empty dictionary
grades = {}

# Create an entry with user input
metric, name, grade = \
    input("Enter exercise, name, grade separated by spaces: ").split()
grades[metric, name] = float(grade)

# Add more entries into the dictionary
grades["test1", "suzy"] = 90
grades["test1", "sally"] = 91.5
grades["test2", "suzy"] = 99
grades["test2", "samantha"] = 88.5
grades["report1", "samantha"] = 90

# Print a sorted list for a given exercise
# Note key[0] references the exercise
print("\nEntries for test1:")
for key in sorted(grades):
    if key[0] == "test1":
        print(key, grades[key])

# Print a sorted list for a given person or persons
# Note key[1] references the names
print("\nEntries for suzy and samantha:")
for key in sorted(grades):
    if key[1] == "suzy" or key[1] == "samantha":
        print(key, grades[key])

# Pick a random entry (just for fun)
print("\nRandom entry:", random.choice(list(grades.items())))

# Print all the items in the dictionary as a list
print("\nAll of the grades printed in a list:")
print(list(grades.items()))

