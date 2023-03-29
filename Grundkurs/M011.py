# Fehlerbehandlung

def doStuff(name: str):
	print(str)

# doStuff()  # TypeError, da ein Parameter fehlt

def rec():
	rec()

# rec()  # RecursionError, da sich die Funktion unendlich oft selbst aufruft

try:  # Hier der Code der Fehler verursachen könnte
	zahl = int(input("Gib eine Zahl ein: "))  # Hier könnten zwei Fehler auftreten: ValueError (keine Zahl), EOFError
except ValueError:  # Hier die einzelnen Fehler abhandeln
	print("Keine Zahl eingegeben")
except EOFError as e:  # Hier der Exception einen Namen geben
	print(e)  # Die Standardfehlermeldung ausgeben
	print("Strg + D gedrückt")
except Exception:  # Alle anderen Fehler fangen
	print("Anderer Fehler")
except:  # Alle anderen Fehler fangen (weniger Code)
	print("Anderer Fehler")
else:  # Wird ausgeführt wenn der try/except Block fehlerfrei ausgeführt wird
	print("Kein Fehler aufgetreten")
finally:  # Wird immer ausgeführt, auch wenn ein Fehler auftritt
	print("Wird immer ausgeführt")

# Raise (throw)
# Eigene Fehler werfen
# Kann auch eigene Fehler werfen (eigene Fehlerklassen)
# raise ValueError("Ein ValueError")  # Mit Nachricht

class CoffeeError(Exception):
	def printStatus(self, status: str):
		print(status)

coffee = 0
try:
	if coffee <= 0:
		raise CoffeeError("Wir haben keinen Kaffee mehr!")
except CoffeeError as e:
	print(e)
	print("Jemand muss Kaffee kaufen")
	e.printStatus("Kein Kaffee mehr")  # e ist ein Exception Objekt vom Typ CoffeeError

# Falscher Input
# 1. Erstelle ein Programm, das den User nach zwei Integern fragt
# 2. Falls der User zwei Integer eingibt sollen diese addiert und das Ergebnis in der Konsole ausgegeben werden und das Programm kann beendet werden
# 3. Falls der Benutzer einen falschen Typen eingibt soll das Programm ihn darauf hinweisen, dass nur Integer akzeptiert werden und ihn erneut nach den Zahlen fragen

# Falscher Index
# 1. Definiere eine beliebige Liste
# 2. Erstelle ein Programm, das es den User fragt, das wievielte Element in der Konsole ausgegeben werden soll
# 3. Falls die Zahl außerhalb des Listen-Indexes liegt soll ein Fehler geworfen und der User darauf hingewiesen werden

# Zu schnell
# 1. Füge der beschleunigen Funktion deiner Fahrzeug-Klasse aus Modul 9 eine eigene Exception hinzu:
# - Sie soll geworfen werden, falls die Höchstgeschwindigkeit überschritten wird
