# Kontrollstrukturen

# Vergleichsoperatoren
# <, >, <=, >=, ==, !=

z1 = 9
z2 = 10

if z1 < z2:
	print("Z1 ist kleiner als Z2")  # Einrückungen müssen passen
	print("If Ende")


if z1 < z2:
	print("Z1 kleiner Z2")
elif z1 > z2:
	print("Z1 größer Z2")


if z1 < z2:
	print("Z1 kleiner Z2")
elif z1 > z2:
	print("Z1 größer Z2")
else:
	print("Z1 gleich Z2")


if z1 < z2:
	print("Z1 kleiner Z2")
	if z1 % 2 == 0:
		print("Z1 ist gerade")  # Hier 2 Einrückungen
	print("X")  # Außerhalb der if

# Logische Operation
# and (&), or (|)
# not (~)
# in: Prüfen ob ein Wert in einer Liste enthalten ist
# is: Schaut ob die Speicheradressen der angegebenen Werte gleich sind
if z1 == 0 and z2 == 0:
	print("Beide Zahlen 0")

liste = [1, 2, 3, 4]
if 3 in liste:
	print("3 ist enthalten")

# Ternary Operator
# Kurzschreibweise für If/Else Konstrukte
a = 10
b = 5
if a < b:
	print("a kleiner b")
else:
	print("a größer b")

print("a kleiner b") if a < b else print("a größer b")

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7]
# Finde heraus welche Liste die längste ist (es können auch mehrere Listen die längsten sein)
if len(list1) > len(list2) and len(list1) > len(list3):
	print("list1 > list2 & list3")
elif len(list2) > len(list1) and len(list2) > len(list3):
	print("list2 > list1 & list3")
else:
	print("list3 > list1 & list2")

# Übung 2
# Nimm die oberen drei Listen und überprüfe ob eine der Listen eine der drei Zahlen enthält: 3, 7, 10
newList = list1 + list2 + list3
if 3 in newList or 7 in newList or 10 in newList:
	print("3, 7, oder 10 ist enthalten")