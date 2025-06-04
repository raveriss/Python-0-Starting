#!/usr/bin/env python3
import time
import datetime
import locale

# On force la locale C pour le nom des mois en anglais
locale.setlocale(locale.LC_TIME, "C")

# 1) Nombre de secondes depuis l'Epoch, arrondi et en notation scientifique
seconds = time.time()
rounded = f"{seconds:,.4f}"
scientific = f"{seconds:.2e}"

print(f"Seconds since January 1, 1970: {rounded} "
      f"or {scientific} in scientific notation")

# 2) Date courante au format '%b %d %Y' (ex : May 20 2025)
print(datetime.datetime.now().strftime("%b %d %Y"))
