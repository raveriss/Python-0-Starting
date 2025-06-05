#!/usr/bin/env python3
import sys


def parse_args():
    """
    Parse command line arguments pour récupérer la chaîne à analyser.
    - Si plus d'un argument est fourni, on lève AssertionError("Too many arguments.").
    - Si exactement un argument est fourni, on le retourne.
    - Si aucun argument n'est fourni, on distingue deux cas :
        • Si stdin n'est pas un terminal (pipe / redirection), on lit tout stdin.
        • Sinon (exécution interactive), on fait input("What is the text to count?\n").
    """
    args = sys.argv[1:]
    if len(args) > 1:
        raise AssertionError("Too many arguments.")
    if len(args) == 1:
        return args[0]

    # Aucun argument : on regarde si on a du contenu sur stdin
    #   - si stdin n'est pas un TTY, on lit tout le flux (jusqu'à EOF)
    #   - sinon (stdin = terminal), on invite l'utilisateur à taper une ligne
    if not sys.stdin.isatty():
        # Lecture brute de tout stdin (jusqu'à EOF)
        return sys.stdin.read()

    # mode interactif
    return input("What is the text to count?\n")


def count_chars(text):
    """
    Compte dans la chaîne text :
      - 'total'       : nombre total de caractères
      - 'upper'       : nombre de lettres majuscules
      - 'lower'       : nombre de lettres minuscules
      - 'digits'      : nombre de chiffres
      - 'spaces'      : nombre d'espaces (isspace())
      - 'punctuation' : nombre de caractères qui ne sont ni alphanumériques ni espaces
    """
    total = len(text)
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    # Tout caractère qui n'est ni alphanum ni espace est compté comme ponctuation
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
    """
    Met en forme la sortie comme demandé :
      The text contains X characters:
      Y upper letters
      Z lower letters
      W punctuation marks
      U spaces
      V digits
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
    try:
        text = parse_args()
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)

    # On essaie de compter ; si la chaîne est trop grosse, on intercepte MemoryError
    try:
        counts = count_chars(text)
    except MemoryError:
        print("MemoryError: impossible to process such a large input.", file=sys.stderr)
        sys.exit(1)

    # Affichage normal
    print(format_output(counts))


if __name__ == "__main__":
    main()
