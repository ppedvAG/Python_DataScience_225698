# Vererbung
# Unterklassen/Oberklassen
# Alle Klassen haben als Oberklasse Object
# Funktionen und Variablen nach unten vererbt

class Lebewesen:
	# __init__ wird vererbt
	def __init__(self, name: str):
		self.name = name
		print("Lebewesen __init__")

	# bewegen wird vererbt
	def bewegen(self, distanz: int):
		print(f"Das Lebewesen hat sich {distanz}m bewegt")

	def __str__(self):
		return f"Mein Name ist {self.name}"

# Mensch ist ein Lebewesen
# Mensch erbt __init__, name und bewegen von Lebewesen
class Mensch(Lebewesen):  # In der Klammer die Oberklasse festlegen
	"""
	Die Mensch Klasse, erbt von Lebewesen und implementiert selbst noch ein Alter.
	"""
	def __init__(self, name: str, alter: int):
		"""
		Der Konstruktor der Mensch Klasse, nimmt Name und Alter als Parameter, ruft den Konstruktor der Lebewesen Klasse auf und schreibt in die Konsole das dieser Konstruktor aufgerufen wurde.

		:param name: Der Name des Menschens.
		:param alter: Das Alter des Menschens.
		"""
		super().__init__(name)  # Mit super() auf Funktionen/Variablen der Oberklasse zugreifen
		self.alter = alter
		print("Mensch __init__")

	def __str__(self):
		"""
		Erzeugt einen Text, der das Objekt im Detail beschreibt.

		:return: Die Textrepräsentation des Objekts.
		"""
		return super().__str__() + f" und ich bin {self.alter} Jahre alt"  # Hier den Output der Oberklasse anhängen


mensch = Mensch("Max", 33)
print(mensch.name)
mensch.bewegen(10)

print(mensch)

# docstring
# Code dokumentieren
# Mit der Maus über einen Typ/eine Methode darübergehen, um den docstring zu lesen
# Unter einen Member gehen und """ schreiben

# Vererbung
# 1. Erstelle die drei folgenden Subklassen der Fahrzeug-Klasse:
#     - PKW
#     - Schiff
#     - Flugzeug
#
# 2. Füge jeweils eine neue passende Eigenschaft hinzu
#
# 3. Überschreibe die Beschreibungs-Funktion der Basis-Klasse um auch die neuen Eigenschaften wiederzugeben
#
# 4. Erstelle jeweils eine Instanz der Klassen und nutze die Beschreibungs Funktionen