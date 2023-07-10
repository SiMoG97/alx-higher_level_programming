#!/usr/bin/python3

"""a module thhat has a MyList class"""


class MyList(list):
    """a class that ingerits list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        myList = self[:]
        myList.sort()
        print(myList)
