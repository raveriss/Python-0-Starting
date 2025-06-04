import sys


def parse_args():
    """Parse command line arguments and return the text to count.

    Raises:
        AssertionError: If more than one argument is provided.

    Returns:
        str: The text to count.
    """
    args = sys.argv[1:]
    if len(args) > 1:
        raise AssertionError("Too many arguments.")
    if len(args) == 1:
        return args[0]
    return input("What is the text to count?\n")


def count_chars(text):
    """Count various categories of characters in the text.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A mapping with keys 'total', 'upper', 'lower', 'punctuation',
        'spaces', 'digits'.
    """
    total = len(text)
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    # On considère comme "ponctuation"
    # tout caractère qui n'est ni alphanumérique ni un espace
    punctuation = sum(1 for c in text if not (c.isalnum() or c.isspace()))
    return {
        'total': total,
        'upper': upper,
        'lower': lower,
        'punctuation': punctuation,
        'spaces': spaces,
        'digits': digits,
    }


def format_output(counts):
    """Format the output string based on character counts.

    Args:
        counts (dict): The character counts.

    Returns:
        str: The formatted output message.
    """
    return (
        f"The text contains {counts['total']} characters:\n"
        f"{counts['upper']} upper letters\n"
        f"{counts['lower']} lower letters\n"
        f"{counts['punctuation']} punctuation marks\n"
        f"{counts['spaces']} spaces\n"
        f"{counts['digits']} digits"
    )


def main():
    """Main entry point of the script."""
    text = parse_args()
    counts = count_chars(text)
    print(format_output(counts))


if __name__ == "__main__":
    main()
