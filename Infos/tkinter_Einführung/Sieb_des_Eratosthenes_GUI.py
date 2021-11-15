'''
Sieb des Eratosthenes
author: Christine Ackerl
date: Nov. 2021
'''

import tkinter as tk

def change_color(index):
    col = kasterln[index].cget('highlightbackground')
    if col == 'black':
        kasterln[index].configure(highlightbackground='red')
    elif col == 'red':
        kasterln[index].configure(highlightbackground='green')
    else:
        kasterln[index].configure(highlightbackground='black')

cell_color='black'

fenster = tk.Tk()

fenster.config(bg='black')

fenster.title('Das Sieb des Eratosthenes')

kasterln={}
for num in range(1,101,1):
    #hintergrund = tk.Frame(fenster,bg=cell_color)
    kasterln[num] = tk.Button(fenster,text=f'{num}',highlightbackground='black',fg='black', width=2, height=2, command=lambda n=num: change_color(n))
    x = int((num-1)/10)
    y_mod = (num % 10)
    if y_mod == 0:
        y = 9
    else:
        y = y_mod-1
    print(x,y)
    #hintergrund.grid(row=x,column=y)
    kasterln[num].grid(row=x,column=y)

fenster.mainloop()