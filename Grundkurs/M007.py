# Module in Python
# Codebibliotheken die wir in unser Projekt einbinden können
# Enthalten nur Code der sich mit dem Thema befasst
# Müssen importiert oder installiert werden

# Wie importiere ich ein Modul?
import turtle as t  # Ganze Bibliothek importieren, mit einem Alias (optional)
from turtle import *  # Einzelnes oder mehrere Skript(e) importieren, hier sind die Methoden im Code direkt verfügbar (ohne Alias)

# from turtle import *
# speed(10)
# color('red', 'blue')
# begin_fill()
# while True:
#     forward(300)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# import turtle as t
# t.speed(10)
# t.color('red', 'blue')
# t.begin_fill()
# while True:
#     t.forward(300)
#     t.left(170)
#     if abs(t.pos()) < 1:
#         break
# t.end_fill()
# t.done()

def countCase(text: str):
	lower, upper, special = 0, 0, 0
	for char in text:
		if char.islower():
			lower += 1
		elif char.isupper():
			upper += 1
		else:
			special += 1
	print(f"Sonderzeichen: {special} | Groß: {upper} | Klein: {lower}")

# Die Variable __name__ enthält den Namen des Skripts
# Wenn das Skript direkt gestartet wurde, wird es __main__ genannt
# Wenn das Skript importiert wird, hat es seinen eigenen Namen
print(__name__)

# In sehr vielen Skripten ist dieser Aufbau vorhanden
# -> Wenn dieses Skript direkt gestartet wurde, führe diesen Code aus
if __name__ == "__main__":
	print("Test")
	print("Ich bin das Hauptskript")
	print(__name__)