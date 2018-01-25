def main():
    my_tuple = (1, 5, 9)
    print(type(my_tuple))
    print(my_tuple)

    for each in my_tuple:
        print(each)

    x, y, z = 9, "eric", 13
    print("x =", x, "y =", y, "z =", z)

    z, y, x = x, y, z
    print("x =", x, "y =", y, "z =", z)


main()
