# List Comprehension
# Schnelle Syntax um eine Liste zu erstellen

# Wir wollen eine Liste von 0-100 haben
ints = list()
for i in range(0, 100):
	ints.append(i)
print(ints)

intsListComprehension = [i for i in range(0, 100)]  # Selbiges wie oben nur in einer Zeile
print(intsListComprehension)

intsModulo2 = [i for i in range(0, 100) if i % 2 == 0]
print(intsModulo2)

max([i for i in range(0, 100) if i % 2 == 0])  # List Comprehension als Parameter

intsHochSichSelbst = [i ** i for i in range(0, 50)]  # Zahl vor Einfügen in die neue Liste noch bearbeiten
print(intsHochSichSelbst)

intsHochSichSelbstGerade = [i ** i for i in range(0, 50) if i ** i % 2 == 0]  # Noch eine Bedingung
print(intsHochSichSelbstGerade)

# Einmaleins Beispielcode
einmaleins = list()
for i in range(1, 11):
	for j in range(1, 11):
		einmaleins.append(f"{i}x{j}={i*j}")
print(einmaleins)

# Mit List Comprehension
einmaleinsLC = [f"{i}x{j}={i*j}" for i in range(1, 11) for j in range(1, 11)]
print(einmaleinsLC)

# List Comprehension mit String Listen
stringListe = ["IcH", "bIN", "eiN", "TeXt"]

stringsGross = [w.upper() for w in stringListe]  # Wort wird bearbeitet vor dem Einfügen
print(stringsGross)

# Alle Wörter mit einem Großbuchstaben am Anfang groß, der Rest klein
stringsGK = [w.upper() if w[0].isupper() else w.lower() for w in stringListe]
print(stringsGK)

# Liste Fehler beheben
stringsTitle = [w.title() if w[0].isupper() else w.lower() for w in stringListe]
print(stringsTitle)

# Alle Wörter mit e finden
stringsE = [w for w in stringListe if "e" in w]
print(stringsE)

# Übung 1
# Schreibe eine List-Comprehension die nur Zahlen aus einer Range von 1 bis inklusive 30 in die neue Liste packt,
# falls die Zahl durch 6 teilbar ist
# Bevor die Zahl in die neue Liste gepackt wird, soll sie um 12 erhöht werden

# Übung 2
# Schreibe eine List-Comprehension die aus einem Text alle Kleinbuchstaben nimmt und Groß in die Liste schreibt

# Übung 3
# Schreibe eine List-Comprehension die aus einem Text alle Anfangsbuchstaben nimmt
# str.split() hier nützlich

# Übung 4
# Schreibe eine List-Comprehension die aus einem Text alle Wörter nimmt die 3 oder weniger Zeichen haben
# str.split() hier nützlich