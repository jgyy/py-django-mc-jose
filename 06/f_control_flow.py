"""
CONTROL FLOW
"""


def main():
    """
    COMPARISON OPERATORS
    """
    print(1 > 2)
    print(1 < 2)
    print(1 <= 4)
    print(1 == "1")
    print("hi" == "bye")
    print(1 != 2)
    print((1 > 2) and (2 < 3))
    print((1 > 2) or (2 < 3))
    print((1 == 2) or (2 == 3))
    if 1 < 2:
        print("Yep!")
    if 1 < 2:
        print("yep!")
    if 1 < 2:
        print("first")
    else:
        print("last")
    if 1 > 2:
        print("first")
    else:
        print("last")
    if 1 == 2:
        print("first")
    else:
        print("Last")
    seq = [1, 2, 3, 4, 5]
    for item in seq:
        print(item)
    for item in seq:
        print("Yep")
    for jelly in seq:
        print(jelly + jelly)
    ages = {"Sam": 3, "Frank": 4, "Dan": 29}
    for key, value in ages.items():
        print("This is the key")
        print(key)
        print("This is the value")
        print(value)
        print("\n")

    tuple_func()


def tuple_func():
    """
    tuple function
    """
    mypairs = [(1, 10), (3, 30), (5, 50)]
    for tup in mypairs:
        print(tup)
    for item1, item2 in mypairs:
        print(item1)
        print(item2)
    i = 1
    while i < 5:
        print("i is: {}".format(i))
        i = i + 1
    print(range(5))
    print(list(range(5)))
    for i in range(5):
        print(i)
    print(range(1, 10))
    print(range(0, 10, 2))
    x_list = [1, 2, 3, 4]
    out = []
    for item in x_list:
        out.append(item ** 2)
    print(out)
    print([item ** 2 for item in x_list])


if __name__ == "__main__":
    main()
