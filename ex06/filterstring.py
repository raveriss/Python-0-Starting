#!/usr/bin/env python3
import sys
from ft_filter import ft_filter

def main():
    """
    Accepts two arguments: a string S and an integer N.
    Outputs a list of words from S whose length is strictly greater than N.
    Uses at least one list comprehension and one lambda.
    Raises AssertionError("the arguments are bad") on wrong count or type of arguments.
    """
    # Validate argument count
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    s = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    words = s.split(" ")
    # Lambda to test word length
    pred = lambda x: len(x) > n
    # Apply ft_filter and list comprehension
    result = [w for w in ft_filter(pred, words)]
    print(result)

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)