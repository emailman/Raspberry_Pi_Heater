# List 1
stooges = ["larry", "curly", "moe"]

# List 2
marxes = ["groucho", "harpo", "chico", "zeppo"]

# List 3
pythons = ["eric", "michael", "john"]

# Combine the lists into a new list
comedians = stooges + marxes + pythons

# Add a person to the list
comedians.append("carlin")

comedians.sort()

for each in comedians:
    print(each)

print("we have listed", len(comedians), "comedians")
