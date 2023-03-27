# List
# Kann mehrere Werte halten (wie Array aus anderen Sprachen)
# Beliebig viele Werte (keine Obergrenze)
# Ist veränderbar, Elemente hinzufügen oder entfernen
# Duplikate sind erlaubt
# Verschiedene Datentypen sind möglich, aber nicht empfehlenswert

meineListe = [1, 2, 3, 4, 'Test', True]
print(meineListe)  # Liste kann einfach mit print ausgegeben werden

# Mit Index auf Elemente zugreifen
print(meineListe[1])
print(meineListe[-1])
print(meineListe[1:3])

# list-Funktion
# Ein Objekt in eine Liste umwandeln
x = list()  # Neue leere Liste erstellen
text = "Ein Text"
print(list(text))  # Jedes Zeichen wird ein Element

# list.append(Element)
# Fügt das Element am Ende der Liste ein
meineListe.append(100)
print(meineListe)

meineListe.append([1, 2, 3])  # List in der List (verschachtelte Liste)
print(meineListe)

# list.extend(Liste)
# Nimmt alle Elemente aus der Liste heraus und fügt sie als einzelne Elemente ans Ende an
meineListe.extend([1, 2, 3])
print(meineListe)

# list.pop(Index)
# Entfernt ein Element am gegebenen Index
meineListe.pop(7)
print(meineListe)

# list.remove(Element)
# Sucht ein Element und entfernt es (erstes Vorkommen)
meineListe.remove(3)
print(meineListe)

meineListe.remove(True)  # Truthy Werte in Python: 1 und True sind True, remove(True) entfernt auch 1
meineListe.insert(0, True)
meineListe.remove(1)  # entfernt True
print(meineListe)

# list.clear()
# Entleert die Liste
meineListe.clear()
print(meineListe)

# list.sort()
# Sortiert die Liste
# Nicht möglich bei gemischten Listen (gemischte Typen)
meineListe = [1, 2, 5, 4, 3]
meineListe.sort()
meineListe.sort(reverse=True)  # Sortierrichtung anpassen
print(meineListe)

# Tupel
# Verhalten sich ähnlich wie Listen
# Sind nicht veränderbar, keine neuen Elemente, bestehende Elemente können nicht geändert werden
# Duplikate sind erlaubt, Datentypen können gemischt sein
# Index vorhanden
# Verschachteln
meinTupel = (1, 2, 3, 4)
print(meinTupel)

# Workaround um Tupel zu ändern
workaround = list(meinTupel)
workaround[0] = 5
meinTupel = tuple(workaround)
print(meinTupel)

# Unpacking
# Löst iterierbare Objekte in ihre einzelnen Elemente auf und danach werden diese in einzelne Variablen geschrieben
# Anzahl der Variablen = Anzahl der Inhalte
# Funktioniert bei String, List, Tuple, ...
unpacking = (1, 2, 3)
a, b, c = unpacking  # Drei Variablen definieren, einzelne Elemente stehen in den entsprechenden Variablen
print(a)
print(b)
print(c)

a = 10  # Einzelne Variablen sind jetzt veränderbar

# Range
# Gibt einen Bereich von Integern an
# Obergrenze exkludiert
# range(Endzahl) -> Sequenz von 0-<Endzahl>
# range(Startzahl, Endzahl) -> Sequenz von <Startzahl> bis <Endzahl>
# range(Startzahl, Endzahl, Schrittgröße) -> Sequenz von <Startzahl> bis <Endzahl> mit <Schrittgröße> Abstand zwischen den Zahlen
meineRange = range(100)
print(meineRange)  # Gibt die Range nicht aus
print(list(meineRange))  # Gibt die Range als Liste aus

print(list(range(50, 100)))  # Sequenz von 50-99

print(list(range(0, 100, 5)))  # 100 nicht dabei, da Obergrenze exkludiert
print(list(range(0, 101, 5)))  # +1 um 100 zu inkludieren

# Set
# Funktioniert ähnlich wie eine Liste
# Kein Index -> keine Anpassung von bestehenden Werten
# Keine Duplikate
# Werte hinzufügen/entfernen möglich
meinSet = {1, 2, 3, 4, 5}
print(meinSet)

# set.add(Element)
# Fügt ein Element am Ende des Sets hinzu
meinSet.add(6)
print(meinSet)

meinSet.add(1)  # Nichts passiert, da die 1 schon existiert
print(meinSet)

# set.pop()
# Entfernt das erste Element
meinSet.pop()
print(meinSet)

# set.remove(Element)
# Entfernt das gegebene Element
meinSet.remove(2)
print(meinSet)

# set.update(Liste)
# Fügt alle Elemente aus der gegebenen Liste in das Set ein, die noch nicht im Set enthalten sind
meinSet.update([1, 2, 3])
print(meinSet)

# Dictionary
# Liste von Key-Value Paaren
# Sind veränderbar
# Keine Key-Duplikate
meinCar = {
	"Brand": "Audi",
	"Model": "A3",
	"Year": 2017
}

print(meinCar)  # Dictionary kann auch wie die oben gegebenen Listentypen geprinted werden
print(meinCar["Brand"])  # Einzelne Werte mit Stringindex angreifen

# Werte verändern
meinCar["Year"] = 2020
print(meinCar)

# Neuen Wert hinzufügen
meinCar["KM"] = 50_000
print(meinCar)

# dictionary.setdefault("Key", Wert)
# Fügt den Eintrag hinzu falls er nicht existiert
# Gibt den Wert zurück falls er schon existiert
meinCar.setdefault("Wheels", 4)
meinCar.setdefault("Wheels", 8)  # Hier wird 4 zurückgegeben
print(meinCar)

# dictionary.get("Key")
# Gibt den Wert vom entsprechenden Schlüssel zurück, ansonsten None
# print(meinCar["ABC"])  # KeyError
print(meinCar.get("ABC"))  # None (Äquivalent zu null)
print(meinCar.get("KM"))  # 50000

# dictionary.items(), dictionary.keys(), dictionary.values()
# Gibt das Dictionary in Teilen zurück
print(meinCar.items())
print(meinCar.keys())
print(meinCar.values())

# dictionary.pop(Element)
# Sucht das Element und entfernt es
meinCar.pop("KM")
print(meinCar)

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
# Kombiniere die drei Listen in eine ganze Liste und schließe Duplikate aus
list4 = list1 + list2 + list3
print(list(set(list4)))

# Übung 2
# Erstelle einen String und wandele ihn in eine Liste um, dabei soll jedes einzelne Zeichen ein Element der Liste werden
print(list("Ein Text"))

# Übung 3
# Lasse eine Liste erstellen die bei 0 beginnt und alle geraden Zahlen bis 20 enthält
# Nicht selbst schreiben, sondern Python machen lassen
print(list(range(0, 21, 2)))