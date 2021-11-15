# Import module
import tkinter as tk

fenster = tk.Tk()
fenster.geometry("1000x1000")
fenster.title('App mit Hintergrundform')

# Bild einlesen
bild = tk.PhotoImage(file="spooky.png")

# Canvas erzeugen
feld = tk.Canvas(fenster, width=400,height=400)

# Canvas platzieren
feld.pack(fill="both", expand=True)

# Hintergrund 'malen'
white_dreieck = feld.create_polygon(0,0,0,1000,1000,1000, fill='blue')

#white_dreieck.move(0,0)

# Bild in Canvas einfügen
#feld.create_image(0, 0, image=bild, anchor="nw")

# Textfeld
feld.create_text(500, 200, text="Hallo! Willkommen zu meiner Coolen App!", font=('Helvetica', 24, 'bold'), fill='black')

# Button erzeugen
knopf = tk.Button(fenster, text="Drück mich!",  bg='black', fg='red')

# Button in Canvas platzieren
button1_canvas = feld.create_window(500, 240, window=knopf)

# App laufen lassen
fenster.mainloop()