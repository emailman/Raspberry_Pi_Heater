myList = [12, 14, 0, -8, 17, 25, 8]

myTripleList =\
    [(each * 3) for each in myList if each >= 0]

for each in myTripleList:
    print(each, "", end="")
print()
