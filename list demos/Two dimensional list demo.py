# Create an empty list
my_list = []

# Set the size of the list
rows = 2
columns = 3

# Scan all the rows
for row in range(rows):
    # Adding a new row
    my_list.append([])

    # Scan all the columns
    for column in range(columns):
        value = float(input("enter a number for row " + str(row) +
                            ", column " + str(column) + ": "))
        # Add the new value to the list in the correct row
        my_list[row].append(value)

print()
print(my_list)

# Show the list as an array
print()
for row in range(rows):
    for column in range(columns):
        print(my_list[row][column], "", end="")
    print()
print()

# Sum each column
for column in range(columns):
    total = 0
    for row in range(rows):
        total += my_list[row][column]
    print("Sum for column", column, "=", total)

# Sum each row
for row in range(rows):
    total = 0
    for column in range(columns):
        total += my_list[row][column]
    print("Sum for row", row, "=", total)
