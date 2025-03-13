def gray_to_binary(gray_str):
    """
    Function to convert a Gray code to its equivalent binary code
    :param gray_str: str: the Gray code to convert (input)
    :return: The converted binary code string (output)
    """
    binary_code = gray_str[0]
    for i in range(1, len(gray_str)):
        binary_bit = str(int(binary_code[i - 1]) ^ int(gray_str[i]))
        binary_code += binary_bit
    return binary_code


if __name__ == "__main__":
    gray_input = input("Enter a Gray code to convert to binary code: ")

    if all(bit in "01" for bit in gray_input):
        result = gray_to_binary(gray_input)
        print(f"The binary equivalent of {gray_input} is {result}")
    else:
        print("Invalid input: Gray code must consist of 0s and 1s only.")
