from tkinter import *

root = Tk()  # Fenster erstellen
root.title("Mein Fenster")
label = Label(text="Ein Text", background="#FF0000")
entry = Entry()

def b1():
	print("B1 gedrückt")

button = Button(text="Test", command=b1)

label.grid()  # Alle Elemente immer hinzufügen
entry.grid()
button.grid()
mainloop()  # mainloop() ganz unten, um das Programm laufen zu lassen