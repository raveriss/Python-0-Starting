def ft_tqdm(lst: range) -> None:
    """
    Implémentation minimaliste de tqdm avec yield, sans imports externes.
    Affiche un pourcentage, une barre de progression statique de 40 caractères,
    et le compteur courant/total. La barre reste visible après la fin.

    :param lst: itérable (range) à parcourir
    :yield: chaque élément de lst
    """
    total = len(lst)
    bar_length = 41
    
    for index, elem in enumerate(lst):
        done = index + 1
        percent = int(done * 100 / total)
        filled = int(done * bar_length / total)
        # Construire la barre : '=' sur la partie remplie, '>' pour l'indicateur, espaces sinon
        bar = '=' * filled + '>' + ' ' * (bar_length - filled)
        # Affichage minimaliste
        print(f"\r{percent:3d}%|[{bar}]| {done}/{total}", end='', flush=True)
        yield elem
    # Saut de ligne final pour conserver la barre affichée
    print()