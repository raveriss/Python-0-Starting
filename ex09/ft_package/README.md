# ft_package

**ft_package** est un package d’exemple fournissant une fonction pour compter les occurrences d’un élément dans une liste.

## Installation

Construisez d’abord les distributions :

```bash
cd ex09
python3 -m build
```
Puis installez via pip :

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
# ou
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```
## Utilisation
```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # affiche 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # affiche 0
```

## Métadonnées
Après installation, vous verrez :

```bash
pip list | grep ft_package
# ft_package    0.0.1
```
```
pip show -v ft_package
```
# Name: ft_package
# Version: 0.0.1
# Summary: A sample test package
# Home-page: https://github.com/eagle/ft_package
# Author: eagle
# Author-email: eagle@42.fr
# License: MIT
# Location: /…/site-packages
# Requires:
# Required-by:
# Metadata-Version: 2.1
# Installer: pip
# Classifiers:
# Entry-points: