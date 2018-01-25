degf = [32, 212, 100, 61, 100, -40]

# This is list comprehension
degc = [round(5 / 9 * (each - 32), 1) for each in degf]

print(degc)

for i in range(len(degf)):
    print(degf[i], "degf =", degc[i], "degc")
