#!/usr/bin/env python3
import sys

# Récupère les arguments sans le nom du script
args = sys.argv[1:]

# Aucun argument : on ne fait rien
if len(args) == 0:
    sys.exit(0)

# Plus d'un argument : erreur
if len(args) > 1:
    msg = "AssertionError: more than one argument is provided"
    print(msg, file=sys.stderr)
    sys.exit(1)

arg = args[0]

# On laisse Python vérifier la syntaxe de l'entier
try:
    n = int(arg)
except ValueError:
    msg = "AssertionError: argument is not an integer"
    print(msg, file=sys.stderr)
    sys.exit(1)

n = int(arg)

# Test de la parité
if n % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
