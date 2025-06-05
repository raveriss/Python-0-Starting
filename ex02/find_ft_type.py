def all_thing_is_obj(object: any) -> int:
    """
    🔎 Détecte le type de l'objet passé en argument et affiche un message
    formaté selon son type. Renvoie toujours 42.

    🧠 Note :
        Si l’usage de fonctions intégrées était autorisé, on pourrait
        utiliser isinstance() (ou match-case dès Python 3.10) pour simplifier
        ces vérifications.
    """

    # 🧬 Récupère dynamiquement le type de l’objet (ex: <class 'list'>)
    obj_type = type(object)

    # 🗂️ Si c’est une liste : affiche le type
    if obj_type is list:
        print(f"List : {obj_type}")

    # 🧱 Si c’est un tuple : affiche le type
    elif obj_type is tuple:
        print(f"Tuple : {obj_type}")

    # 🔁 Si c’est un ensemble : affiche le type
    elif obj_type is set:
        print(f"Set : {obj_type}")

    # 🗃️ Si c’est un dictionnaire : affiche le type
    elif obj_type is dict:
        print(f"Dict : {obj_type}")

    # 🧾 Si c’est une chaîne de caractères : message personnalisé
    elif obj_type is str:
        print(f"{object} is in the kitchen : {obj_type}")

    # ❓ Si le type n’est pas reconnu dans cette liste
    else:
        print("Type not found")
    return 42


# if __name__ == "__main__":
#     # No action when run directly
#     pass
