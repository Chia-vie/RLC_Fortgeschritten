import tkinter as tk

class Seite1():
    def __init__(self, fenster, container):
        self.s1_rahmen = tk.Frame(fenster)
        label = tk.Label(self.s1_rahmen, text='Das ist Seite 1')
        label.pack(side='top', fill='both', expand='True')
        self.s1_rahmen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    def show(self):
        self.s1_rahmen.lift()

class Seite2():
    def __init__(self, fenster, container):
        self.s1_rahmen = tk.Frame(fenster)
        label = tk.Label(self.s1_rahmen, text='Das ist Seite 2')
        label.pack(side='top', fill='both', expand='True')
        self.s1_rahmen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    def show(self):
        self.s1_rahmen.lift()

class Seite3():
    def __init__(self, fenster, container):
        self.s1_rahmen = tk.Frame(fenster)
        label = tk.Label(self.s1_rahmen, text='Das ist Seite 3, sie zeigt eine rote, furchteinflößende Schrift! ', fg='red')
        label.pack(side='top', fill='both', expand='True')
        self.s1_rahmen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    def show(self):
        self.s1_rahmen.lift()

def haupt_ansicht(fenster):
    buttonframe = tk.Frame(fenster)
    container = tk.Frame(fenster)
    buttonframe.pack(side="top", fill="x", expand=False)
    container.pack(side="top", fill="both", expand=True)

    s1 = Seite1(fenster, container)
    s2 = Seite2(fenster, container)
    s3 = Seite3(fenster, container)

    b1 = tk.Button(buttonframe, text="Page 1", command=s1.show)
    b2 = tk.Button(buttonframe, text="Page 2", command=s2.show)
    b3 = tk.Button(buttonframe, text="Page 3", command=s3.show)

    b1.pack(side="left")
    b2.pack(side="left")
    b3.pack(side="left")

    s1.show()


fenster = tk.Tk()
haupt_ansicht(fenster)
fenster.geometry("400x400")
fenster.mainloop()
