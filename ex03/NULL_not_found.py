#!/usr/bin/env python3

"""
Module: NULL_not_found
Defines a function to identify "null-like" values
and display their value and type.
"""


def NULL_not_found(object: any) -> int:
    """
    Print the value and type for recognized null-like objects:
      - None      → "Nothing"
      - float NaN → "Cheese"
      - 0         → "Zero"
      - ''        → "Empty"
      - False     → "Fake"

    Returns:
        0 if the object is one of the recognized null-like values,
        1 otherwise (and prints "Type not Found").

    Note:
        If built-in functions were allowed,
        it would be clever to use isinstance()
        to simplify type checks (e.g., isinstance(object, float)).
    """
    # Check for None
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    # Check for NaN (only float where self-inequality holds)
    if type(object) is float and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0
    # Check for boolean False
    if type(object) is bool and object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    # Check for integer zero
    if type(object) is int and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    # Check for empty string
    if type(object) is str and object == "":
        print(f"Empty: {type(object)}")
        return 0
    # Unrecognized type
    print("Type not Found")
    return 1


# if __name__ == "__main__":
#     # No action when run directly
#     pass
