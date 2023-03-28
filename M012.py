# Lambda Expressions
from functools import reduce

# Lambdas sind anonyme Funktionen die in einer Variable gespeichert werden können (u.a.)
# In anderen Sprachen =>, ->
# In Python haben wir das Lambda Keyword
# Eigenschaften
# - Kein Name
# - Beliebig viele Parameter
# - Optionaler Return Wert
# - Darf nur eine Expression enthalten
# - Keine Schleifen, kein break/continue

add = lambda x, y: x + y
print(add(4, 6))

def summe(x, y):
	return x + y

summeL = lambda *zahlen: sum(zahlen)  # auch * und ** Argumente sind möglich
print(summeL(1, 2, 3, 4, 5))

def lambdaPar(le):  # Lambda als Parameter
	print(le(1, 2, 3))  # Verwenden wie Lambda Expression

lambdaPar(summeL)  # Lambda übergeben

# filter(), map(), reduce()

# filter()
# Filtert die Liste nach dem Kriterium der Lambda Expression
# Syntax: filter(Lambda, Liste)
ints = list(range(0, 100))
print(filter(lambda x: x % 2 == 0, ints))  # filter object als Ergebnis -> Umwandeln mit list()
print(list(filter(lambda x: x % 2 == 0, ints)))

from M009 import Person
personen = [Person("Max", 35), Person("Test", 23), Person("Abc", 50)]

print(list(filter(lambda p: p.alter > 30, personen)))  # Finde alle Personen die mindestens 30 Jahre als sind

# map()
# Wandelt die Liste in eine neue Form um
# Syntax: map(Lambda, Liste)
print(list(map(lambda x: x * 3, ints)))  # map object als Ergebnis -> Umwandeln mit list()

print([x * 3 for x in ints])  # obiges Beispiel mit List Comprehension

# Wir wollen die int Liste zu einer String Liste umwandeln
print(list(map(lambda x: str(x), ints)))

# Extra Spalte hinzufügen
print(list(map(lambda x: (x, x ** x), ints)))

# reduce()
# Wandelt die Liste in ein einzelnes Ergebnis um
# Syntax: reduce(Lambda, List)
print(reduce(lambda ergebnis, zahl: ergebnis + zahl, ints))

texte = ["Hallo", "ich", "bin", "ein", "Text"]

print(reduce(lambda vollerText, t: f"{vollerText} {t}", texte))

# Addition und Subtraktion
# 1. Erstelle jeweils eine Lambda-Funktion die zwei Zahlen addiert bzw subtrahiert
#
# 2. Gebe die Ergebnisse in der Konsole aus

# Filter
# 1. Nutze die filter() Funktion um eine Liste mithilfe von Lambdas nach folgenden Merkmalen zu filtern:
#
#     - Nur gerade Zahlen sollen in der neuen Liste enthalten sein
#     - Nur ungerade Zahlen sollen in der neuen Liste enthalten sein
#     - Nur Vielfache von 4 sollen enthalten sein
#
# 2. Gebe die Listen in der Konsole aus

# Map
# 1. Nutze die map() Funktion um die Werte eine Liste mithilfe von Lambdas zu quadrieren
#
# 2. Nutze die map(Funktion) um die Werte einer Liste zu halbieren
#
# 3. Gib die Listen in der Konsole aus

# Reduce
# 1. Nutze die reduce() Funktion aus dem functools Modul und eine Lambda Funktion um folgendes zu erreichen:
#
#     - Summiere die Werte einer Sequenz
#     - Subtrahiere die Werte einer Sequenz
#
# 2. Lass das Ergebnis in der Konsole ausgeben