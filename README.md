**Projet Piscine Python for Data Science**
**Aperçu du projet**

Ce dépôt regroupe mes exercices **00** à **09** de la Piscine Python for Data Science de l’école 42. Il a pour objectif de renforcer mes compétences en Python et de m’habituer aux bonnes pratiques de développement (modularité, style, tests). Tous les modules sont conçus pour fonctionner avec Python 3.10.

**Prérequis**
- **Python 3.10** installé et configuré
- **pip** pour installer les dépendances
- **flake8** (alias `norminette`) pour vérifier la conformité du code aux standards PEP 8 et aux consignes du projet

- Pour l’exercice **08**, j’utilise la bibliothèque **tqdm** :
```bash
pip install tqdm
```
**Structure du dépôt**
```bash
├── ex00/  # Exercice 00 : script Hello.py
├── ex01/  # Exercice 01 : format_ft_time.py
├── ex02/  # Exercice 02 : find_ft_type.py
├── ex03/  # Exercice 03 : NULL_not_found.py
├── ex04/  # Exercice 04 : whatis.py
├── ex05/  # Exercice 05 : building.py
├── ex06/  # Exercice 06 : ft_filter.py et filterstring.py
├── ex07/  # Exercice 07 : sos.py
├── ex08/  # Exercice 08 : Loading.py
├── ex09/  # Exercice 09 : package ft_package
└── README.md
```
**Comment j’exécute les exercices**
Chaque exercice se trouve dans son répertoire `exNN`. Pour lancer le script principal :
```bash
cd ex00
python Hello.py
```
**Exemples d’utilisation**
- **Exercice 00** (greetings) :
```bash
python ex00/Hello.py
```
- **Exercice 04** (pair/impair) :
```bash
python ex04/whatis.py 14   # "I'm Even."
python ex04/whatis.py Hi!  # AssertionError
```
Pour chaque exercice, je me réfère aux énoncés détaillés fournis dans le PDF de la Piscine.

**Mes règles générales de développement**
1. **Modularité** : je n’écris pas de code dans la portée globale. J’utilise une fonction `main()` avec le bloc :
```py
if __name__ == "__main__":
    main()
```
2. **Documentation** : chaque fonction comporte une docstring explicative
3. **Gestion des erreurs** : je capture toutes les exceptions ; toute exception non gérée invalide l’exercice
4. **Style** : je respecte les normes PEP 8 via `flake8`/`norminette`

**Licence**
MIT

**Contact**
Pour toute question, j’invite à ouvrir une issue ou à me contacter directement.
