# Klassen und Objekte

# Alles in Python ist ein Objekt
# Jedes Objekt hat alle Funktionen die in der jeweiligen Klasse vorgegeben werden

i = 12  # Variable i mit 12 (Objekt)
i.as_integer_ratio()
print(type(i))  # Typ vom Objekt <class: 'int'>

# isinstance
# Überprüft ob eine Variable einen bestimmten Typ hat
print(isinstance(i, int))  # True
print(isinstance(i, str))  # False
print(isinstance(i, object))  # True

# Klassen
# Bauplan für Objekte

class Person:
	x = 500  # Klassenvariable, ist global für alle Objekte der Klasse und generell auch ohne Objekt setzbar über den Klassennamen (static)

	# Funktion definieren, jedes Objekt dieser Klasse hat die Funktion
	# self: muss bei jeder Funktion in einer Klasse der erste Parameter sein
	# self = Objekt selber (this)
	def speak(self, text: str):
		print(f"Mein Name ist: {text}")

	# __init__: Der Konstruktor, kommt vom Objekt
	def __init__(self, name: str, alter: int):  # Hier Parameter festlegen
		self.name = name  # Hier neue Variablen anlegen, werden als Instanzvariablen deklariert
		self.alter = alter
		print("Das Objekt wurde erstellt")

	def __str__(self):
		return f"Mein Name ist {self.name} und mein Alter ist {self.alter}"


person = Person("Max", 33)  # Neues Person Objekt erstellen ohne new
person.speak("Max")
print(person.name)
print(person.alter)

person.wohnort = "Eine Straße 1"  # Neue Werte in ein Objekt schreiben ist möglich in Python
print(person.wohnort)

# Wenn ein Objekt geprinted wird, wird die __str__() Methode verwendet
# Kann überschrieben werden genauso wie __init__()
print(person)  # Output von __str__(): <__main__.Person object at 0x00000172125BBFD0>

p2 = Person("", 111)
Person.x = 1000  # Variable wird bei beiden Person Objekten geändert

del person.wohnort
# print(person.wohnort)

# Fahrzeug-Klasse
# 1. Erstelle eine Fahrzeug-Klasse
#
# 2. Diese Klasse soll typische Eigenschaften eines Fahrzeuges enthalten:
#     - Fahrzeug-Name
#     - Preis
#     - Maximale Geschwindigkeit
#     - Derzeitige Geschwindigkeit
#     - Motorzustand (An/Aus)
#
# 3. Die Klasse soll auch folgende Methoden enthalten:
#     - Beschleunigen(Erhöhe bzw Verringere die Derzeitige Geschwindigkeit aber übersteige nicht das Maximum)
#     - StarteMotor
#     - StoppeMotor
#     - Beschreibung (Gibt alle Informationen über die Klasse wieder)
#
# 4. Erstelle eine Instanz der Klasse und nutze die Beschreibungs Funktion