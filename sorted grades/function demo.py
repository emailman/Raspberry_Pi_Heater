def rectangle_calc(x, y):
    area = x * y
    perimeter = 2 * (x + y)

    return area, perimeter


def main():
    try:
        length = float(input("Enter the length of a rectangle: "))
        width = float(input("Enter the width of a rectangle: "))
        units = input("Enter the units: ")

        area_, perimeter_ = rectangle_calc(length, width)

        print("length =", length, units, ", width =", width, units)
        print("area = ", area_, "sq", units, ", perimeter = ",
              perimeter_, units)

        print(rectangle_calc(length, width))

    except ValueError:
        print("You messed up")
        exit(1)


main()
