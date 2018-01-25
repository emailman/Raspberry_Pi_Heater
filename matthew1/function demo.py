def f(x):
    m = 2
    b = 1
    y = (m * x) + b
    return y


def main():
    for x in range(12, 0, -2):
        print("x =", x, ": y =", f(x))


main()
