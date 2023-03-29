# venv
# Virtuelle Umgebung
# Ermöglicht uns, Pakete zwischen Projekten zu separieren
# Wird aus der Standardumgebung gebildet

# Mehrzeilige Kommentare (/**/) existieren nicht, es gibt nur # oder '''

# Variablen nehmen ihren Typ anhand des Inhalts an
x = 5  # Hat jetzt den Typ int
x = "Ein Text"  # Hat jetzt den Typ string

# Datentypen

# Integer (int)
# Ganze Zahl, beliebig groß

grosseZahl = 38572937592375923759234759237583265104678

# Float (float)
# Kommazahl
kommazahl = 893472275923759.329587982375

# String (str)
# Text mit "", ''
text1 = "Ein Text"
text2 = 'Zwei Text'

# Boolean (bool)
# True/False, großgeschrieben
wahr = True
falsch = False

# Complex
# Komplexe Zahlen, haben den Buchstaben J
c = 12j + 5

# Stringfunktionen
text = "Max Mustermann"

# Ausgaben auf die Konsole machen
print(text)

# string.count(Text)
# Zählt die Vorkommnisse (Case-Sensitive)
print(text.count("M"))  # 2

# string.lower(), string.upper()
# Macht den Text Lowercase/Uppercase
print(text.lower().count('m'))  # 3
print(text.upper().count('M'))  # 3

# string.islower(), string.isupper()
# Gibt einen bool zurück, ob der ganze Text Lowercase/Uppercase ist
print(text.isupper())
print(text.islower())

# Index
# Auf bestimmte Stellen greifen mit [Zahl]
# Funktionert auch bei Strings, gibt einen String als Ergebnis (statt Char wie in anderen Sprachen)
print(text[0])  # M
print(text[0].isupper())

# type(Variable)
# Den Typ einer Variable herausfinden
# Auch nützlich für Typvergleiche
print(type(text))  # <class 'str'>

# len(Variable)
# Gibt die Länge eines iterierbaren Objektes zurück
print(len(text))  # 14

# Negativer Index
# Objekt von rechts angreifen
# -1 = Das erste Element von rechts
print(text[-1])  # n
print(text[-2])  # n

# Range Operator
# Bereiche eines Objekts auswählen
# Wird mit : bezeichnet
# Obergrenze exkludiert
print(text[0:5])  # Max M
                  # 01234
print(text[1:5])  # ax M
print(text[-5:-1])  # rman -> -4, -3, -2, -1
print(text[4:])  # Von 4 bis zum Ende
print(text[:3])  # Bis 3

# string.isalpha(), string.isnumeric(), string.isalnum()
# Prüft ob ein String nur aus Buchstaben, nur aus Zahlen, oder nur aus beiden besteht (ohne Sonderzeichen)
print(text.isalpha())  # False, Leerzeichen
print(text.isnumeric())  # False
print(text.isalnum())  # False, Leerzeichen

# Arithmetische Operatoren in Python
# +, -, *, /, %
# **: Potenzierung
# //: Ganzzahldivision
z1 = 4
z2 = 9

print(z1 + z2)
z1 += z2  # Verändert tatsächlich Werte

print(z1)
print(z2)

print(z2 ** z2)  # 9^9

print(z1 / z2)  # 1.444444
print(z1 // z2)  # 1

# Arithmetik mit Strings
print(text1 + text2)
text1 += text2
print(text1)

# Strings multiplizieren
print(text1 * 10)
text1 *= 10

# Übung1
# Lege drei numerische Variablen an, addiere sie zusammen und schreibe das Ergebnis in eine neue Variable
# Potenziere danach die Variable mit sich selbst und schreibe das Ergebnis erneut in eine Variable
z1 = 2
z2 = 4
z3 = 7
ergebnis = z1 + z2 + z3
potenz = ergebnis ** ergebnis

# Übung2
# Nimm die potenzierte Zahl aus Übung1 und stelle fest ob diese Restlos durch 2 teilbar (gerade) ist
mod = potenz % 2

# Übung3
# Lege zwei Variablen an: Vorname befüllt mit Max und Nachname befüllt mit Mustermann
# Verbinde diese zwei Variablen und zähle danach die Buchstaben 'M' und 'm'
# Das Ergebnis soll 3 sein
vorname = "Max"
nachname = "Mustermann"
gesamt = vorname + nachname
print(gesamt.lower().count("m"))

# Übung4
# Schreibe deinen Vornamen ohne Großbuchstaben in eine Variable
# Verwende danach diese Variable, und gib diese mit dem ersten Buchstaben groß geschrieben aus
name = 'lukas'
print(name[0].upper() + name[1:])
print(name[0].upper() + name[1:len(name)])
print(name.title())
print(name.capitalize())