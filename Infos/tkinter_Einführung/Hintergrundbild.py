# Import module
import tkinter as tk

fenster = tk.Tk()
fenster.geometry("1000x1000")
fenster.title('App mit Hintergrundbild')

# Bild einlesen
bild = tk.PhotoImage(file="spooky.png")

# Canvas erzeugen
feld = tk.Canvas(fenster, width=400,height=400)

# Canvas platzieren
feld.pack(fill="both", expand=True)

# Bild in Canvas einfügen
feld.create_image(0, 0, image=bild, anchor="nw")

# Textfeld
feld.create_text(500, 500, text="Hallo! Willkommen zu meiner Coolen App!", font=('Helvetica', 24, 'bold'), fill='white')

# Button erzeugen
knopf = tk.Button(fenster, text="Drück mich!",  bg='black', fg='red')

# Button in Canvas platzieren
button1_canvas = feld.create_window(500, 540, window=knopf)

# App laufen lassen
fenster.mainloop()