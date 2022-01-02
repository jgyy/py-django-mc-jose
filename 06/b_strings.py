"""
Strings
"""


def main():
    """
    Creating a String
    """
    print("hello")
    print("This is also a string")
    print("String built with double quotes")
    print("I'm using single quotes, but will create an error")
    print("Now I'm ready to use the single quotes inside a string!")
    print("Hello World")
    print("Hello World 1")
    print("Hello World 2")
    print("Use \n to print a new line")
    print("\n")
    print("See what I mean?")
    print(len("Hello World"))
    s_str = "Hello World"
    print(s_str)
    print(s_str[0])
    print(s_str[1])
    print(s_str[2])
    print(s_str[1:])
    print(s_str)
    print(s_str[:3])
    print(s_str[:])
    print(s_str[-1])
    print(s_str[:-1])
    print(s_str[::1])
    print(s_str[::2])
    print(s_str[::-1])
    print(s_str)
    print(s_str + " concatenate me!")
    s_str = s_str + " concatenate me!"
    print(s_str)
    letter = "z"
    print(letter * 10)
    print(s_str.upper())
    print(s_str.lower())
    print(s_str.split())
    print(s_str.split("W"))
    p_str = "some string"
    print(f"Insert another string with curly brackets: {p_str}")
    print(f"This is a string with an {p_str}")
    print(f"One: {p_str}, Two: {p_str}, Three: {p_str}")
    a_str = "alpha"
    b_str = "beta"
    c_str = "charlie"
    print(f"Object 1: {a_str}, Object 2: {b_str}, Object 3: {c_str}")


if __name__ == "__main__":
    main()
