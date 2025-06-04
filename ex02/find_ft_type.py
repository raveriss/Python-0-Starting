def all_thing_is_obj(object: any) -> int:
    """
    Detects the type of the given object and prints a formatted message.
    Returns 42 always.

    Note:
        If built-in functions were allowed,
        t would be clever to use isinstance()
        (or match-case in Python 3.10) to simplify type checks.
    """
    obj_type = type(object)
    if obj_type is list:
        print(f"List : {obj_type}")
    elif obj_type is tuple:
        print(f"Tuple : {obj_type}")
    elif obj_type is set:
        print(f"Set : {obj_type}")
    elif obj_type is dict:
        print(f"Dict : {obj_type}")
    elif obj_type is str:
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")
    return 42


if __name__ == "__main__":
    # No action when run directly
    pass
