# pyright: reportInvalidTypeForm=false
def ft_tqdm(lst: range) -> None:
    """
    Implémentation minimaliste de tqdm avec l'opérateur `yield`, sans aucun import externe.
    La fonction affiche un pourcentage, une barre de progression fixe de 41 caractères,
    ainsi qu'un compteur du type courant/total. La barre reste visible après la fin de l'itération.

    Bien que la fonction utilise `yield` (ce qui en fait techniquement un générateur),
    la signature `-> None` est imposée par le sujet. Elle est donc conservée malgré son incompatibilité
    avec le comportement réel de la fonction. Cette anomalie peut être ignorée dans ce contexte pédagogique.

    :param lst: itérable de type range à parcourir
    :yield: chaque élément de lst, un par un
    """
    total = len(lst)
    bar_length = 41

    for index, elem in enumerate(lst):
        done = index + 1
        percent = int(done * 100 / total)
        filled = int(done * bar_length / total)
        # Construction de la barre de progression
        bar = '=' * filled + '>' + ' ' * (bar_length - filled)
        # Affichage minimaliste
        print(f"\r{percent:3d}%|[{bar}]| {done}/{total}", end='', flush=True)
        yield elem
    # Saut de ligne final pour conserver la barre affichée
    print()
