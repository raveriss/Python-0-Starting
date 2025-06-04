#!/usr/bin/env python3
"""Exercice 00 : démonstration basique des structures de données Python."""

# def print_set_coherent(s: set) -> None:
#  Affiche les éléments du set avec 'Hello'
# en premier, suivi de l'élément campus."""
#     # Récupère l'élément différent de 'Hello'
#     other = next(elem for elem in s if elem != "Hello")
#     print(f"{{'Hello', '{other}'}}")

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
    print(ft_set)
    print(ft_dict)
except Exception:
    """Signale toute erreur sans interrompre le script."""
    print("Une erreur est apparue")
