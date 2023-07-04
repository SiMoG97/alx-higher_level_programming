#!/usr/bin/python3
"""
    LockedClass class
"""


class LockedClass:
    """
        a class LockedClass with no class or object attribute,
        that prevents the user from dynamically creating new instance attr,
        except if the new instance attribute is called first_name
    """
    __slots__ = ("first_name",)
