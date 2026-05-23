import sys as sy


def count_and_print(text: any):
    """
        Counting and printing element of a string
    """

    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for i in text:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i in "'.,;:?!":
            punctuation += 1
        elif i.isspace():
            spaces += 1
        elif i.isdigit():
            digits += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits ")


def main():
    """
        This is the main function yayyyyyyyyyyyyyyy
    """

    if len(sy.argv) > 2:
        print(AssertionError("AssertionError: too much arguments"))
        sy.exit()
    elif len(sy.argv) <= 1:
        try:
            text = input("What is the text to count?\n")
        except EOFError:
            print(AssertionError("AssertionError: EOF error"))
            sy.exit()
    else:
        text = sy.argv[1]

    count_and_print(text)


if __name__ == "__main__":
    main()
