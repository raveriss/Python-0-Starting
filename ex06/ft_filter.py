#!/usr/bin/env python3
import sys


def ft_filter(function, iterable):
    """
ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]


# Assigner la docstring de la fonction native filter à ft_filter
ft_filter.__doc__ = filter.__doc__


def main():
    """
    Points de test pour valider ft_filter et comparer au filter natif.
    Chaque test recrée ses données pour éviter l’épuisement des itérables.
    """
    # Définition des tests : (nom, prédicat, factory d'itérable)
    def is_even(x):
        return x % 2 == 0

    def is_odd(x):
        return x % 2 != 0

    def greater_than_three(x):
        return x > 3

    def contains_a(s):
        return 'a' in s

    def non_empty(lst):
        return bool(lst)

    def always_false(x):
        return False

    # Générateurs de données pour chaque cas :
    def gen_1_to_6():
        return [1, 2, 3, 4, 5, 6]

    def gen_range_6():
        return range(6)

    def gen_strings_with_a():
        return ('apple', 'banana', 'cherry', 'date', '')

    def gen_nested_lists():
        return [[], [1], [], [0, 2], []]

    def gen_range_10():
        return list(range(10))

    def gen_mixed_truth():
        return [0, False, '', 'Bonjour', 42, None]

    def gen_small_list():
        return [1, 2, 3, 4]

    # 2) On construit ensuite le tableau de tests sans aucun lambda :

    test_cases = [
        ("Nombres pairs", is_even, gen_1_to_6),
        ("Nombres impairs", is_odd, gen_1_to_6),
        ("> 3 dans un range", greater_than_three, gen_range_6),
        ("Chaînes contenant 'a'", contains_a, gen_strings_with_a),
        ("Listes imbriquées non-vides", non_empty, gen_nested_lists),
        ("Nombres >5 dans une liste", greater_than_three, gen_range_10),
        ("Filtre par vérité (function=None)", None, gen_mixed_truth),
        ("Toujours False", always_false, gen_small_list),
    ]

    for name, pred, data_factory in test_cases:
        data1 = data_factory()
        data2 = data_factory()
        attendu = list(filter(pred, data1))
        obtenu = ft_filter(pred, data2)
        print(f"Cas de test : {name}")
        print(f" Données : {data2!r}")
        print(f" Prédicat : {pred}")
        print(f" Attendu : {attendu}")
        print(f" Obtenu : {obtenu}")
        print(f" {'✅ Succès' if obtenu == attendu else '❌ Échec'}\n")

    # Test d'une fonction non-callable (doit lever TypeError)
    try:
        ft_filter(123, [1, 2, 3])
        print("❌ Échec: aucune exception pour function non-callable")
    except TypeError:
        print("✅ Succès: TypeError levée pour function non-callable")

    # Vérification de la docstring
    if ft_filter.__doc__ == filter.__doc__:
        print("✅ Succès: docstring correspond à celle de filter")
    else:
        print("❌ Échec: docstring ne correspond pas à celle de filter")


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"Erreur lors des tests: {e}")
        sys.exit(1)
