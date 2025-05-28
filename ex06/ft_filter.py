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
    test_cases = [
        ("Nombres pairs",                      lambda x: x % 2 == 0,         lambda: [1,2,3,4,5,6]),
        ("Nombres impairs",                    lambda x: x % 2 != 0,         lambda: [1,2,3,4,5,6]),
        ("> 3 dans un range",                  lambda x: x > 3,              lambda: range(6)),
        ("Chaînes contenant 'a'",              lambda s: 'a' in s,           lambda: ('apple','banana','cherry','date','')),
        ("Listes imbriquées non-vides",        lambda lst: bool(lst),        lambda: [[], [1], [], [0,2], []]),
        ("Nombres >5 dans une liste",          lambda x: x > 5,              lambda: list(range(10))),  # rectifié
        ("Filtre par vérité (function=None)",  None,                         lambda: [0, False, '', 'Bonjour', 42, None]),
        ("Toujours False",                     lambda x: False,              lambda: [1,2,3,4]),
    ]

    for name, pred, data_factory in test_cases:
        data1   = data_factory()
        data2   = data_factory()
        attendu = list(filter(pred, data1))
        obtenu  = ft_filter(pred, data2)
        print(f"Cas de test : {name}")
        print(f"  Données    : {data2!r}")
        print(f"  Prédicat   : {pred}")
        print(f"  Attendu    : {attendu}")
        print(f"  Obtenu     : {obtenu}")
        print(f"  {'✅ Succès' if obtenu == attendu else '❌ Échec'}\n")

    # Test d'une fonction non-callable (doit lever TypeError)
    try:
        ft_filter(123, [1,2,3])
        print("❌ Échec: aucune exception pour function non-callable")
    except TypeError:
        print("✅ Succès: TypeError levée pour function non-callable")

    # Vérification de la docstring
    if ft_filter.__doc__ == filter.__doc__:
        print("✅ Succès: la docstring de ft_filter correspond à celle de filter")
    else:
        print("❌ Échec: la docstring de ft_filter ne correspond pas à celle de filter")

if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"Erreur lors des tests: {e}")
        sys.exit(1)
