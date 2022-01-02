"""
Tuples and Booleans
"""


def main():
    """
    Constructing Tuples
    """
    t_tuple = (1, 2, 3)
    print(len(t_tuple))
    t_tuple = ("one", 2)
    print(t_tuple)
    print(t_tuple[0])
    print(t_tuple[-1])
    print(t_tuple.index("one"))
    print(t_tuple.count("one"))
    a_bool = True
    print(a_bool)
    print(1 > 2)


if __name__ == "__main__":
    main()
