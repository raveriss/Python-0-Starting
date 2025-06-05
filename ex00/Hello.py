#!/usr/bin/env python3
"""Exercice 00 : démonstration basique des structures de données Python."""

# 🎲 Remarque : l'ordre d'affichage des éléments du set (`ft_set`) peut varier
# à chaque exécution. Cela vient de son implémentation via une hash table
# (table de hachage), combinée à la hash randomization activée par défaut
# depuis Python 3.3 pour des raisons de sécurité. Résultat : l'ordre n'est
# pas garanti même si le contenu reste identique.

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

try:
    """Applique des changements :
    - liste : remplace l’élément à l’index 1
    - tuple : recrée un nouveau tuple
    - set : redéfinit l’ensemble avec un nouvel élément campus
    - dict : met à jour la valeur associée à la clé 'Hello'
    """
    ft_list[1] = "World!"
    ft_tuple = (ft_tuple[0], "France!")
    ft_dict["Hello"] = "42Paris!"
    ft_set = {"Hello", "Paris!"}

    print(ft_list)
    print(ft_tuple)

    # ⚠️ Remarque : l'ordre d'affichage des éléments du set peut varier à
    # chaque exécution. Cela est dû à l'utilisation d'une table de hachage
    # (hash table) combinée à la hash randomization (introduite en Python
    # 3.3 pour la sécurité).
    # Ainsi, même si ft_set contient toujours les mêmes éléments, leur ordre
    # n'est pas garanti.
    print(ft_set)

    print(ft_dict)
except Exception:
    """Signale toute erreur sans interrompre le script."""
    print("Une erreur est apparue")
