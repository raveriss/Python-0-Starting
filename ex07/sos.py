# Import du module sys pour accéder aux arguments de la ligne de commande et à sys.exit
import sys

# Dictionnaire de correspondance entre caractères et code Morse
NESTED_MORSE = {
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

# Fonction de conversion d'une chaîne de caractères en code Morse
def encode_to_morse(text: str) -> str:
    # On normalise le texte en majuscules pour correspondre aux clés du dictionnaire
    text = text.upper()
    # Liste pour stocker les symboles Morse
    morse_symbols = []
    # Pour chaque caractère de la chaîne
    for char in text:
        # On vérifie que le caractère existe dans le dictionnaire
        if char not in NESTED_MORSE:
            # Si non, on lève une erreur indiquant des arguments invalides
            raise AssertionError("the arguments are bad")
        # Sinon, on ajoute le code Morse correspondant à la liste
        morse_symbols.append(NESTED_MORSE[char])
    # On retourne la chaîne finale, symboles séparés par des espaces
    return " ".join(morse_symbols)

# Fonction principale du script
def main():
    # Vérification du nombre d'arguments : doit être exactement 2 (le script + un paramètre)
    if len(sys.argv) != 2:
        # Si incorrect, on lève une erreur
        raise AssertionError("the arguments are bad")
    # Conversion du seul argument en Morse
    result = encode_to_morse(sys.argv[1])
    # Affichage du résultat sur la sortie standard
    print(result)

# Point d'entrée du script
if __name__ == "__main__":
    try:
        # Exécution de la fonction main
        main()
    except AssertionError as e:
        # Interception de l'erreur pour afficher uniquement le message sans traceback
        print(f"AssertionError: {e}")
        # Sortie avec code d'erreur pour indiquer l'échec
        sys.exit(1)
