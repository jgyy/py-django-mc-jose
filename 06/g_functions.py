"""
FUNCTIONS
"""


def main():
    """
    def Statements
    """

    def my_func(param1="default"):
        """
        Docstring goes here.
        """
        print(param1)

    my_func("not default")

    def hello():
        print("hello")

    hello()

    def give_me_hello():
        return "hello"

    result = give_me_hello()
    print(result)
    print(give_me_hello)

    def even_check(num):
        print(f"I'm checking to see if {num} is even!")
        print(num % 2 == 0)

    even_check(41)

    def hello_you(name="Default Name"):
        return "Hello, " + name

    result = hello_you()
    print(result)

    def add_even_only(num1, num2):
        """
        INPUT: Two numbers
        OUTPUT: False if both numbers are not even,
        the sum if both numbers ar even
        """
        if (num1 % 2 != 0) or (num2 % 2 != 0):
            return False
        return num1 + num2

    x_res = add_even_only(1, 2)
    y_res = add_even_only(2, 2)
    print(x_res)
    print(y_res)


if __name__ == "__main__":
    main()
