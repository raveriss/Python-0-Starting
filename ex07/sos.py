import sys

def encode_to_morse(text: str) -> str:
    # Dictionnaire de correspondance entre caractères et code Morse
    morse_map = {
        " ": "/",  # Espace traduit par slash
        "A": ".-",   "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".",    "F": "..-.", "G": "--.",  "H": "....",
        "I": "..",   "J": ".---", "K": "-.-",  "L": ".-..",
        "M": "--",   "N": "-.",   "O": "---",  "P": ".--.",
        "Q": "--.-", "R": ".-.",  "S": "...",  "T": "-",
        "U": "..-",  "V": "...-", "W": ".--",  "X": "-..-",
        "Y": "-.--", "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",
    }

    text = text.upper()
    morse_symbols = []
    for char in text:
        if char not in morse_map:
            raise AssertionError("the arguments are bad")
        morse_symbols.append(morse_map[char])
    return " ".join(morse_symbols)

def main():
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    result = encode_to_morse(sys.argv[1])
    print(result)

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
