# Funktionen

# Ein Code Block der nur beim Aufruf ausgeführt wird

def hallo():  # Funktion ohne Parameter
	print("Hallo")

hallo()
hallo()

def halloName(name):  # Funktion mit Parameter
	print(name)

halloName("Lukas")
halloName(123)
halloName(True)
halloName([1, 2, 3])  # Alles möglich

def halloNameStr(name: str):  # Hier einen Hinweis geben was die Variable ist mit <Name>: <Typ
	print(name)
	# print(name.upper())  # Stringfunktionen jetzt möglich, stürzt ab wenn User keinen String übergibt

halloNameStr(123)  # Funktioniert trotzdem


def addiere(x: int, y: int):
	return x + y

summe = addiere(20, 30)
print(summe)

summeFloat = addiere(5.5, 2.2)  # Hier sind Typen auch egal
print(summeFloat)

def dividiere(x: int, y: int) -> int:  # Hier Rückgabetyp explizit angeben
	return x / y  # Hier Fehler aber ist bei der Ausführung kein Problem

print(dividiere(5, 2))

zahl: int  # Auch Variablen können mit Typ deklariert werden
zahl = "Text"
print(zahl)

# Default Werte
# Bei einem Parameter angeben was der Standardwert ist, und muss dann beim Aufruf diesen nicht übergeben
def subtrahiere(x: int, y: int, yMinusX=False):
	if ~yMinusX:
		return x - y
	else:
		return y - x

subtrahiere(8, 2)  # Default Parameter weggelassen
subtrahiere(9, 3, True)  # Default Parameter überschrieben

# Parameter in anderer Reihenfolge angeben (Positional Arguments)
subtrahiere(y=6, x=3, yMinusX=True)

# Arbitrary Arguments
# * Parameter
# Gibt die Möglichkeit, beliebig viele Parameter zu übergeben
def summiere(*numbers: int) -> int:
	return sum(numbers)

summiere(1, 2, 3)  # 3 Parameter
summiere(1, 2, 3, 4, 5, 6, 7)  # 7 Parameter

# Unpacking Operator
# Teilt die Liste in ihre Einzelteile auf
zahlen = [1, 2, 3, 4, 5]
# summiere(zahlen)  # Nicht möglich
print(summiere(10, *zahlen, 10))  # Zerlegung erzwingen
print(summiere(*range(100)))  # Besonders nützlich bei Range


def buchstabiere(*wort):
	for zeichen in wort:
		print(zeichen)

buchstabiere("Text")  # Einzelnes Element für Tupel -> tupel("Text")
buchstabiere(*"Text")  # Zerlegung auch für Strings möglich -> tupel("T", "e", "x", "t")

# a, b, c = [1, 2, 3, 4, 5]  # Zu viele Werte
a, *b, c = [1, 2, 3, 4, 5]  # Von links und rechts werden die Elemente 1:1 gematcht, alle anderen kommen in das * Element
print(a)
print(b)
print(c)

def halloGuests(**guests):
	for k, v in guests.items():
		print(f"Nummer: {k}, Name: {v}")

halloGuests(Gast1="Andreas", Gast2="Julius", Gast3="Lukas")  # Beliebig viele Key-Value Paare übergeben

def passTest():
	pass  # Mach garnix

def parSlash(z1, z2, /, z3, z4):  # Erzwingt das z1 und z2 am Anfang angegeben werden müssen
	return z1 + z2 + z3

# parSlash(z2=1, z4=3, z3=5, z1=10)  # Reihenfolge anpassbar
parSlash(3, 6, z4=10, z3=5)  # z1 und z2 sind jetzt fix


# Übung 1:
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# Und uns die größte dieser Zahlen zurückgibt
def Max(*numbers):
	m = 0  # numbers[0] um auch negative Zahlen zu berücksichtigen
	for i in numbers:
		if i > m:
			m = i
	return m

def Maximum(*numbers):
	return max(numbers)

# Übung 2:
# Wir wollen eine Funktion erstellen, die einen String als Parameter erhält
# Die Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht
# Bonus: Die Funktion soll zusätzlich zählen wie viele Sonderzeichen (Nummern inkludiert) enthalten sind und das
# ebenfalls ausgeben
# Sonderzeichen: 4 | Groß: 3 | Klein: 12
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

countCase("Ein Text")