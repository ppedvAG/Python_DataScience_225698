# Decorator
# Funktion an eine andere Funktion anhängen
# Werden mit @<Name> hinzufügen
import time


def test():  # Funktionen sich auch Objekte
	pass

print(test)

def TestDecorator(func):  # func: Die Funktion die später den Decorator erhalten wird
	def wrapper():  # Funktion in der Funktion möglich, da in Python alles Objekte sind
		print("Vor der Funktion")
		func()
		print("Nach der Funktion")
	return wrapper  # Hier kommt der fertige Decorator heraus (ohne Klammern)

def hello():
	print("Hallo")

decorated = TestDecorator(hello)
decorated()

# Kurzform

@TestDecorator
def bye():
	print("Goodbye")

bye()


# Decorator mit Parametern
def DoTwice(func):
	def wrapper(*args, **kwargs):  # *args, **kwargs decken alle möglichen Parameter ab
		func(*args, **kwargs)
		func(*args, **kwargs)
	return wrapper

@DoTwice
def printAddiere(x, y):
	print(x + y)

printAddiere(3, 4)
printAddiere(y=5, x=1)

# Decorator mit Rückgabewert
def DoTwiceReturn(func):
	def wrapper(*args, **kwargs):
		return func(*args, **kwargs), func(*args, **kwargs)  # Einfach return hinzufügen
	return wrapper

@DoTwiceReturn
def sub(x, y):
	return x - y

(z1, z2) = sub(3, 5)
print(z1)
print(z2)

# Ausführungszeit messen
def MeasureTime(func):
	def wrapper(*args, **kwargs):
		starttime = time.time()
		func(*args, **kwargs)
		endttime = time.time()
		print(f"{endttime - starttime}s vergangen")
	return wrapper

@MeasureTime
def sumNumbers(*args):
	return sum(args)

sumNumbers(*range(10000000))

# Properties
# Geben uns die möglich die Programmierparadigmen von anderen Sprachen zu übernehmen (private Variablen, Getter & Setter)
# Wir können in Python allerdings nicht dazu gezwungen werden, die Getter/Setter oder "private Variablen" einzuhalten

class Square:
	def __init__(self, a: float):
		self._seitenlaenge = a  # Einigung, dass Variablen mit _ "privat" sind und nicht von außen geändert werden sollten

	@property
	def seitenlaenge(self):
		print("Die Seitenlaenge wurde angegriffen")
		return self._seitenlaenge

	@seitenlaenge.setter
	def seitenlaenge(self, neu: float):
		if neu < 0 or neu > 100:
			print("Fehler")
		else:
			self._seitenlaenge = neu


q = Square(5)
print(q.seitenlaenge)
q.seitenlaenge = 10  # Normalerweise können Funktionen nicht gesetzt werden, aber durch setter ist das möglich