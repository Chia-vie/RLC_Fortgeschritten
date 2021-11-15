import tkinter as tk

class Willkommen():
    def __init__(self, fenster, container):
        self.s1_rahmen = tk.Frame(fenster)
        label = tk.Label(self.s1_rahmen, text='Willkommen! Schön dass du da bist!')
        label.pack(side='top', fill='both')
        self.s1_rahmen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        geheim = Geheime_Bibliothek(fenster, container)
        ohne = Ohne_Passwort(fenster, container)

        b1 = tk.Button(self.s1_rahmen, text="Geheime Bibliothek öffnen", command=geheim.show)
        b2 = tk.Button(self.s1_rahmen, text="Ohne Passwort fortfahren", command=ohne.show)

        b1.pack(side='top')
        b2.pack(side='top')
        #b3.pack(side="left")
    def show(self):
        self.s1_rahmen.lift()

class Geheime_Bibliothek():
    def __init__(self, fenster, container):
        self.s2_rahmen = tk.Frame(fenster)
        label = tk.Label(self.s2_rahmen, text='Willkommen in der geheimen Bibliothek!')
        label.pack(side='top', fill='both', expand='True')
        self.s2_rahmen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    def show(self):
        self.s2_rahmen.lift()

class Ohne_Passwort():
    def __init__(self, fenster, container):
        self.s3_rahmen = tk.Frame(fenster)
        label = tk.Label(self.s3_rahmen, text='Das ist Seite 3, sie zeigt eine rote, furchteinflößende Schrift! ', fg='red')
        label.pack(side='top', fill='both', expand='True')
        self.s3_rahmen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    def show(self):
        self.s3_rahmen.lift()

def haupt_ansicht(fenster):
    buttonframe = tk.Frame(fenster)
    container = tk.Frame(fenster)
    buttonframe.pack(side="top", fill="x", expand=False)
    container.pack(side="top", fill="both", expand=True)

    w = Willkommen(fenster, container)

    b1 = tk.Button(buttonframe, text="Startseite", command=w.show)

    b1.pack(side="left")

    w.show()


fenster = tk.Tk()

fenster.geometry("400x400")

haupt_ansicht(fenster)

fenster.mainloop()
