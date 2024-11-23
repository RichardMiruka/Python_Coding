def main():
    x = int(input("What is X? "))
    # print ("X squared is", x*x)

    # or use the square function
    print("X squared is", square(x))


def square(
    n,
):  # Define a function called square that takes a number as input and returns the square of that number
    return n * n


main()
