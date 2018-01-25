def largest(x, y):
    if x > y:
        return x
    else:
        return y


def main():
    print(largest("eric", "fred"))

    print(type(largest("fred", "eric")))


main()
