import M007
import sys
import numpy

from M007 import countCase as cc

# m.countCase("Ein Text")
cc("Ein Text")

# Module-Searchpath
# 1. Im selben Ordner wie das derzeitige Skript
# 2. In der venv des Projekts
# 3. PYTHONPATH, Ordner in dem die Standardinstallation ist
# 4. Extra Ordner die bei anlegen des Projekts konfiguriert werden können
# Wenn nach Punkt 4 immer noch nichts gefunden wurde -> ModuleNotFoundError
print(sys.path)

# sys Modul
# Alle möglichen Informationen zur Umgebung
# z.B.: Python Version, Suchpfade, Platform (OS), ...
print(sys.version)
print(sys.platform)
# sys.exit(0)  # Programm beenden, Exitcodes: 0 -> Ok, nicht 0 -> nicht Ok

# Extra Module installieren
# 1. Entweder per Terminal (pip)
# pip install <Name>
# pip uninstall <Name>
# 2. Per Python Package Manager

def main():
	print("M007b ist das Hauptskript")
	numpy.floor(5.5)

if __name__ == "__main__":
	main()