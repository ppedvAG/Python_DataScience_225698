import json
import os.path as path
from typing import IO

# In- & Output

# input(string)
# Wartet auf einen Input vom Benutzer, wird mit Enter bestätigt
# Eingabe kommt in eine Variable
# Programm bleibt stehen, bis der User ein Eingabe macht

# name = input("Gib deinen Namen ein: \t")  # Escape-Sequenzen: \t -> Tabulator, \n -> Zeilenumbruch
# alter = int(input("Gib dein Alter ein: \n"))
# print(f"Dein Name ist {name} und du bist {alter} Jahre alt")

# open(Pfad, Modus)
# Öffnet einen Stream zu einer Datei mit dem gewählten Modus
# w: Write, Overwrite
# r: Read
# a: append
# x: Create
# r+/w+: Read/Write, Erstellt die Datei neu wenn sie nicht existiert

writeF = open("Test.txt", "w+")  # Rückgabewert: IO Objekt
writeF.write("Ein Text\n")
writeF.write("Zwei Text")

writeF.close()  # Stream schließen, wenn er geöffnet bleibt kann die Datei nicht verändert werden

readF = open("Test.txt", "r")
lines = readF.readlines()  # Den Inhalt des Files in eine String-Liste einlesen

print(lines)

with open("Test.txt", "w+") as writeF:
	writeF.write("Ein Text\n")
	writeF.write("Zwei Text")
# Hier wird der Stream geschlossen

# os.path: Skript für Pfadoperationen
if path.exists("Test.txt"):
	with open("Test.txt", "r") as readF:
		lines = readF.readlines()
		print(lines)
else:
	writeF = open("Test.txt", "w+")  # Rückgabewert: IO Objekt
	writeF.write("Ein Text\n")
	writeF.write("Zwei Text")

# rstring
# Raw string
# Interpretiert alles als string (Escape Sequenzen, Backslash, ...)
# Besonders nützlich bei Pfaden
rstring = r"C:\Users\lk3\source\repos\Python_DataScience_2023_03_27"
print(rstring)

# Json
numList = { "Key1": 1, "Key2": 2, "Key3": 3 }
jsonStr = json.dumps(numList)  # dump: Schreibt direkt in ein File, dumps: Schreibt in einen String
print(type(json.loads(jsonStr)))  # type(): Gibt den Typ des Objekts zurück

with open("Test.json", "w+") as wFile:
	json.dump(numList, wFile)  # Schreibt direkt in ein File

with open("Test.json", "r") as rFile:
	readObj = json.load(rFile)  # Lädt direkt von einem File
	print(readObj)

# Übung:
# Funktion die dem User die Möglichkeiten (w, r, a) gibt
# User soll eine davon auswählen über input()
# Wenn der User keine valide Möglichkeit eingibt, soll die Eingabe wiederholt werden bis der User eine valide Eingabe eingibt
# Danach soll einfach das File geöffnet werden
def auswahl() -> IO:
	while True:  # Endlosschleife bis der User etwas korrektes eingibt
		choice = input("Gib w, r oder a ein: ")
		# if choice == "w" or choice == "r" or choice == "a":
		if choice in ["w", "r", "a"]:  # in statt if/or
			break
	print("Valide Eingabe, File wird geöffnet")
	return open("Test.txt", choice)

auswahl()