"""
Dictionaries
"""


def main():
    """
    Make a dictionary with {} and : to signify a key and a value
    """
    my_dict = {"key1": "value1", "key2": "value2"}
    print(my_dict["key2"])
    my_dict = {"key1": 123, "key2": [12, 23, 33], "key3": ["item0", "item1", "item2"]}
    print(my_dict["key3"])
    print(my_dict["key3"][0])
    print(my_dict["key3"][0].upper())
    print(my_dict["key1"])
    my_dict["key1"] = my_dict["key1"] - 123
    print(my_dict["key1"])
    my_dict["key1"] -= 123
    print(my_dict["key1"])
    d_dict = {}
    d_dict["animal"] = "Dog"
    d_dict["answer"] = 42
    print(d_dict)
    d_dict = {"key1": {"nestkey": {"subnestkey": "value"}}}
    print(d_dict["key1"]["nestkey"]["subnestkey"])
    d_dict = {"key1": 1, "key2": 2, "key3": 3}
    print(d_dict.keys())
    print(d_dict.values())
    print(d_dict.items())


if __name__ == "__main__":
    main()
