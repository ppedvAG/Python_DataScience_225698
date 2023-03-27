# Schleifen

# While Schleife
# Läuft solange die Bedingung true ist
# Zähler sollte dabei sein (in der Regel)
i = 0
while i < 10:
	print(i)
	i += 1  # Hier gibt es kein ++
else:
	print("Nach der Schleife")  # Wird ausgeführt, wenn die Schleife fehlerfrei beendet wurde (ohne break)


j = 0
while True:
	print(j)
	j += 1
	if j == 500:
		break  # Springt aus der Schleife heraus
else:
	print("Nach der Schleife")  # Kann nicht ausgeführt werden


# for Schleife
# Verhält sich wie foreach in anderen Sprachen
# Über eine Collection iterieren (String, List, Tupel, ...)
liste = [1, 2, 3, 4]
for x in liste:  # x = derzeitiges Element
	print(x)
	print("Mehrere Zeilen")

for z in range(0, 100):  # "Normale" for-Schleife
	print("for: " + str(z))

for z in range(50, 100, 2):
	print("for+2: " + str(z))

for c in "Ein Text":  # Über einen Text iterieren
	print(c)

# break und continue
# break: Aus der Schleife springen
# continue: Rest der Schleife überspringen und zum Kopf zurück gehen
for z in range(0, 10):
	if z == 5:
		continue  # Bei z = 5 wird print übersprungen
	print(z)

# fstring
# Formatted String
# String in den Code eingebaut werden kann
# f"{Code}"
for z in range(0, 10):
	print(f"for: {z}")  # Hier mit f den String markieren

for z in range(0, 10):
	print(f"for: {z}, {z % 3 == 0}")

# Ich möchte pro Schleifendurchlauf immer die Zahl selbst, Zahl^2 und die Gleichung ausgeben
for z in range(0, 10):
	# Ohne fstring
	print("Die Zahl ist: " + str(z))
	print("Die Zahl^2 ist: " + str(z * z))
	print("Die Gleichung ist: " + str(z) + " * " + str(z) + " = " + str(z*z))

	# Mit fstring
	print(f"Die Zahl ist: {z}")
	print(f"Die Zahl^2 ist: {z * z}")
	print(f"Die Gleichung ist: {z} * {z} = {z * z}")

# Übung 1
# FizzBuzz
# 1. Schleife schreiben, die von 0 bis inklusive 100 hochzählt
# 2. Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
# Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# 1
# 2
# Fizz
#  4
# Buzz
# ...
# 14
# FizzBuzz

# Übung 2
# Schreibe eine Schleife die dir alle Zahlen von 1 bis 200 zur Verfügung stellt
# Lass dir jede Zahl erst in der kardinalen und dann daneben in der ordinalen Schreibweise darstellen
# Zahl + Endung 'st', 'nd', 'rd' oder 'th'
# 1st, 2nd, 3rd, 4th, ..., 21st, 22nd, 23rd, 24th
# Bonus: Berücksichtige alle Zahlen die mit 11, 12 oder 13 enden

# Übung 1:
# Stoppuhr
# Bevor die Minute hochtickt, müssen die Sekunden einmal eine vollkommenen Umdrehung hinter sich gebracht haben
# time.sleep(Float) Funktion hier nützlich

# Übung 2:
# Erstelle eine Schleife die das kleine Einmaleins von 1 bis 10 berechnet, und jeden einzelnen
# Schritt in der Konsole ausgibt
# "1 x 1 = 1"
# ...
# "5 x 5 = 25"
# ...
# "10 x 10 = 100"