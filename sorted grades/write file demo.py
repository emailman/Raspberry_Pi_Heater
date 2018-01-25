def main():
    file_handle_1 = open("data.txt", "w")
    file_handle_1.writelines(["hello world", "new world"])
    # file_handle_1.write("goodbye world")
    file_handle_1.close()

    file_handle_2 = open("data.txt", "r")
    lines = file_handle_2.readlines()
    print(lines)
    file_handle_2.close()

    for line in lines:
        print(line)


main()
