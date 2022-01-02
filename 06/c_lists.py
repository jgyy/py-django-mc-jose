"""
Lists
"""


def main():
    """
    Assign a list to an variable named my_list
    """
    my_list = [1, 2, 3]
    my_list = ["A string", 23, 100.232, "o"]
    print(len(my_list))
    my_list = ["one", "two", "three", 4, 5]
    print(my_list[0])
    print(my_list[1:])
    print(my_list[:3])
    print(my_list + ["new item"])
    print(my_list)
    my_list = my_list + ["add new item permanently"]
    print(my_list)
    print(my_list * 2)
    mylist = [1, 2, 3]
    mylist.append("append me!")
    mylist.pop(0)
    popped_item = mylist.pop()
    print(popped_item)
    print(mylist)
    new_list = ["a", "e", "x", "b", "c"]
    print(new_list)
    new_list.reverse()
    print(new_list)
    new_list.sort()
    print(new_list)


if __name__ == "__main__":
    main()
