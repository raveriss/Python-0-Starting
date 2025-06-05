#!/usr/bin/env python3
import time
import datetime
import locale

# 🌍 On force la locale "C" (locale POSIX) pour que les noms de mois
# soient affichés en anglais, quel que soit le système (utile pour les
# scripts portables ou les évaluations automatisées).
locale.setlocale(locale.LC_TIME, "C")

# ⏱️ Récupère le nombre de secondes depuis l'Epoch (1er janv. 1970).
# La variable `seconds` est un float avec des décimales.
seconds = time.time()

# 🔢 Formate le nombre de secondes avec 4 décimales et des virgules
# pour la lisibilité humaine (ex: 1,234,567.8910).
rounded = f"{seconds:,.4f}"

# 🧪 Représentation en notation scientifique (ex: 1.23e+09),
# pratique pour les très grandes valeurs.
scientific = f"{seconds:.2e}"

# 🖨️ Affiche les deux représentations côte à côte : lisible et scientifique.
print(f"Seconds since January 1, 1970: {rounded} "
      f"or {scientific} in scientific notation")

# 📅 Affiche la date actuelle au format abrégé : "May 20 2025".
# `%b` = mois abbr., `%d` = jour, `%Y` = année à 4 chiffres.
print(datetime.datetime.now().strftime("%b %d %Y"))
