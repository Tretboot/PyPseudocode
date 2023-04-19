# PyPseudocode ist ein kleines Programm, das zufälligen Pseudocode generiert
# Es hat eine grafische Benutzeroberfläche mit drei Buttons: Copy Code, Regenerate und Degenerate
# Es generiert Pseudocode in Mandelbrot Fraktalform
# Es kann unendlich scrollenden oder zoomenden Code generieren
# Es kann die Anzahl der generierten Zeilen einstellen

# Importiere die benötigten Module
import random
import tkinter
from tkinter import *
import threading
import time


# Definiere eine Funktion, die einen zufälligen Pseudocode-Befehl zurückgibt
def zufalls_befehl():
  # Wähle eine zufällige Zahl zwischen 1 und 10 aus
  zahl = random.randint(1, 10)
  # Falls die Zahl 1 ist, gib eine Zuweisung zurück
  if zahl == 1:
    # Wähle einen zufälligen Variablennamen aus
    name = random.choice(["x", "y", "z", "a", "b", "c"])
    # Wähle einen zufälligen Wert aus
    wert = random.choice([0, 1, 2, 3, "wahr", "falsch", "nichts"])
    # Gib die Zuweisung zurück
    return name + " = " + str(wert)
  # Wenn die Zahl 2 ist, gib eine Schleife zurück
  if zahl == 2:
    # Wähle einen zufälligen Schleifentyp aus
    typ = random.choice(["for", "solange"])
    # Sollte der Typ for sein, gib eine for-Schleife zurück
    if typ == "for":
      # Wähle einen zufälligen Variablennamen aus
      name = random.choice(["i", "j", "k", "n", "m"])
      # Wähle einen zufälligen Startwert aus
      start = random.randint(0, 10)
      # Wähle einen zufälligen Endwert aus
      ende = random.randint(start + 1, start + 10)
      # Gib die for-Schleife zurück
      return "for " + name + " von " + str(start) + " bis " + str(ende) + ":"
    # Wenn der Typ solange ist, gib eine solange-Schleife zurück
    if typ == "solange":
      # Wähle eine zufällige Bedingung aus
      bedingung = random.choice(["x < y", "y > z", "z == a", "a != b", "b < c", "c > x"])
      # Gib die solange-Schleife zurück
      return "solange " + bedingung + ":"
  # Wenn die Zahl 3 ist, gib eine Bedingung zurück
  if zahl == 3:
    # Wähle eine zufällige Bedingung aus
    bedingung = random.choice(["x < y", "y > z", "z == a", "a != b", "b < c", "c > x"])
    # Gib die Bedingung zurück
    return "if " + bedingung + ":"
  # Wenn die Zahl 4 ist, gib eine Funktion zurück
  if zahl == 4:
    # Wähle einen zufälligen Funktionsnamen aus
    name = random.choice(["funktion1", "funktion2", "funktion3", "funktion4"])
    # Wähle eine zufällige Anzahl von Parametern aus
    anzahl = random.randint(0, 3)
    # Erstelle eine leere Liste von Parameternamen
    parameter = []
    # for jede Anzahl von Parametern:
    for i in parameter:
      # Wähle einen zufälligen Parameternamen aus und füge ihn der Liste hinzu
       parameter.append(random.choice(["p", "q", "r", "s"]))
    # Erstelle einen String aus den Parameternamen mit Kommas getrennt
    parameter_string = ", ".join(parameter)
    # Gib dieligen Variablennamen aus
    name = random.choice(["i", "j", "k", "n", "m"])
    # Wähle eine zufällige Anzahl von Iterationen aus
    anzahl = random.randint(1, 10)
    # Gib die Schleife zurück
    return "for " + name + " in range(" + str(anzahl) + "):"
  # Wenn die Zahl 3 ist, gib eine Bedingung zurück
  if zahl == 3:
    # Wähle einen zufälligen Ausdruck aus
    ausdruck = random.choice(["x > y", "y < z", "z == a", "a != b", "b und c", "c oder x"])
    # Gib die Bedingung zurück
    return "if " + ausdruck + ":"
  # Wenn die Zahl 4 ist, gib eine Funktion zurück
  if zahl == 4:
    # Wähle einen zufälligen Funktionsnamen aus
    name = random.choice(["funktion1", "funktion2", "funktion3", "funktion4", "funktion5"])
    # Wähle eine zufällige Anzahl von Parametern aus
    anzahl = random.randint(0, 3)
    # Erstelle eine Liste von Parameternamen
    parameter = []
    for i in range(anzahl):
      # Wähle einen zufälligen Parameternamen aus
      parameter.append(random.choice(["p", "q", "r", "s", "t"]))
    # Gib die Funktion zurück
    return "definiere " + name + "(" + ", ".join(parameter) + "):"
  # Wenn die Zahl 5 ist, gib einen Funktionsaufruf zurück
  if zahl == 5:
    # Wähle einen zufälligen Funktionsnamen aus
    name = random.choice(["funktion1", "funktion2", "funktion3", "funktion4", "funktion5"])
    # Wähle eine zufällige Anzahl von Argumenten aus
    anzahl = random.randint(0, 3)
    # Erstelle eine Liste von Argumenten
    argumente = []
    for i in range(anzahl):
      # Wähle ein zufälliges Argument aus
      argumente.append(random.choice([0, 1, 2, 3, "wahr", "falsch", "nichts"]))
    # Gib den Funktionsaufruf zurück
    return name + "(" + ", ".join(str(arg) for arg in argumente) + ")"
  # Wenn die Zahl 6 ist, gib einen Kommentar zurück
  if zahl == 6:
    # Gib den Kommentar zurück
    return "# Ich habe keine Ahnung, was diese Funktion macht"
  # Wenn die Zahl 7 ist, gib eine leere Zeile zurück
  if zahl == 7:
    # Gib die leere Zeile zurück
    return ""
  # Wenn die Zahl 8 ist, gib eine Einrückung zurück
  if zahl == 8:
    # Gib die Einrückung zurück
    return "\t"
  # Wenn die Zahl 9 ist, gib eine Ausrückung zurück
  if zahl == 9:
    # Gib die Ausrückung zurück
    return "\b"
  # Wenn die Zahl 10 ist, gib eine Rückkehr zurück
  if zahl == 10:
    # Gib die Rückkehr zurück
    return "\n"

# Definiere eine Funktion, die einen Pseudocode in Mandelbrot Fraktalform generiert
def mandelbrot_pseudocode():
  # Erstelle eine leere Liste von Zeilen
  zeilen = []
  # Erstelle eine Variable for die aktuelle Einrückungsstufe
  einrückung = ""
  # Erstelle eine Variable for die maximale Anzahl von Zeilen
  max_zeilen = int(input("Wie viele Zeilen möchtest du generieren? "))
  
# Erstelle ein tkinter-Fenster
fenster = tkinter.Tk()
# Setze den Fenstertitel
fenster.title("PyPseudocode")
# Setze die Fenstergröße
fenster.geometry("800x600")

# Erstelle eine Textbox, um den Pseudocode anzuzeigen
text = tkinter.Text(fenster)
# Setze die Textbox-Größe
text.pack(expand=True, fill="both")
# Setze die Textbox-Schriftart
text.config(font=("Courier", 12))

# Definiere eine Funktion, die den Pseudocode in der Textbox kopiert
def kopiere_code():
  # Hole den gesamten Text aus der Textbox
  code = text.get("1.0", "end")
  # Kopiere den Text in die Zwischenablage
  fenster.clipboard_clear()
  fenster.clipboard_append(code)

# Definiere eine Funktion, die neuen Pseudocode in der Textbox generiert
def generiere_code():
  # Lösche den alten Text aus der Textbox
  text.delete("1.0", "end")
  # Setze eine Variable for die Anzahl der Zeilen
  zeilen = 20
  # Setze eine Variable for die Einrückungsebene
  ebene = 1
  # Wiederhole für jede Zeile
  for i in  range (zeilen):
    # Generiere einen zufälligen Befehl
    befehl = zufalls_befehl()
    # Füge Leerzeichen entsprechend der Einrückungsebene hinzu
    befehl = " " * (ebene * 4) + befehl
    # Füge den Befehl in die Textbox ein
    text.insert("end", befehl + "\n")
    # Wenn der Befehl eine Schleife ist, erhöhe die Einrückungsebene um 1
    if befehl.startswith("for") or befehl.startswith("solange"):
      ebene = ebene + 1
    # Wenn die Einrückungsebene größer als 0 ist, verringere sie zufällig um 1 mit einer Wahrscheinlichkeit von 0.5
    if ebene > 0 and random.random() < 0.5:
      ebene = ebene - 1

# Definiere eine Funktion, die den Pseudocode in der Textbox degeneriert
def degeneriere_code():
  # Hole den gesamten Text aus der Textbox
  code = text.get("1.0", "end")
  # Ersetze alle Buchstaben durch zufällige Zeichen aus dem Mandelbrot Fraktalset
  zeichen = [" ", ".", ",", "-", "+", "*", "/", "%", "^", "(", ")", "[", "]", "{", "}"]
  neuer_code = ""
  for c in code:
    if c.isalpha():
      neuer_code = neuer_code + random.choice(zeichen)
    else:
      neuer_code = neuer_code + c
  # Lösche den alten Text aus der Textbox
  text.delete("1.0", "end")
  # Füge den neuen Text in die Textbox ein
  text.insert("1.0", neuer_code)

# Diese Funktion wird aufgerufen, wenn der Benutzer auf den "Nightmode" Button klickt
def toggle_nightmode():
    if text.config('background')[-1] == 'black':
        text.config(background='white', foreground='black')
    else:
        text.config(background='black', foreground='green')

# Diese Funktion wird aufgerufen, wenn der Benutzer auf den "Matrix ON" Button klickt
def matrix_on():
    # Setze die Hintergrund- und Textfarbe auf schwarz und grün
    text.config(background='black', foreground='green')
    
    # Starte einen neuen Thread, um den Code automatisch laufen zu lassen
    matrix_thread = threading.Thread(target=matrix_run)
    matrix_thread.start()

# Diese Funktion wird in einem separaten Thread ausgeführt und lässt den Code automatisch laufen
def matrix_run():
    # Warte 1 Sekunde vor dem Start
    time.sleep(1)
    
    # Hole den aktuellen Text aus dem Textfeld
    code = text.get("1.0", END)
    
    # Lösche den aktuellen Text aus dem Textfeld
    text.delete("1.0", END)
    
    # Füge den Text Zeile für Zeile zum Textfeld hinzu
    for line in code.split("\n"):
        text.insert(END, line + "\n")
        text.see(END)
        time.sleep(0.1)

# Erstelle einen Button, um den Pseudocode zu kopieren
kopieren = tkinter.Button(fenster, text="Copy Code", command=kopiere_code)
# Setze den Button unten links im Fenster
kopieren.pack(side="left")

# Erstelle einen Button, um neuen Pseudocode zu generieren
generieren = tkinter.Button(fenster, text="Regenerate", command=generiere_code)
# Setze den Button unten in der Mitte im Fenster
generieren.pack(side="left")

# Erstelle einen Button, um den Pseudocode zu degenerieren
degenerieren = tkinter.Button(fenster, text="Degenerate", command=degeneriere_code)
# Setze den Button unten rechts im Fenster
degenerieren.pack(side="left")

# Erstelle einen Button für den "Nightmode"
nightmode_button = tkinter.Button(fenster, text="Nightmode", command=toggle_nightmode)
# Setze den Button unten rechts im Fenster
nightmode_button.pack(side="left")

# Erstelle einen Button für "Matrix ON"
matrix_button = tkinter.Button(fenster, text="Matrix ON", command=matrix_on)
# Setze den Button ganz rechts im Fenster
matrix_button.pack(side="right")

# Generiere initialen Pseudocode in der Textbox
generiere_code()

# Starte die tkinter-Hauptschleife
fenster.mainloop()
