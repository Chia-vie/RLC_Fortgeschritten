import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from Geheim import Geheim

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text_eingabe.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_eingabe.insert(tk.END, text)
    window.title(f"Text Editor Application - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_eingabe.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Mein geheimes Tagebuch - {filepath}")

def encrypt():
    geheim = Geheim(text_eingabe.get(1.0, tk.END))
    geheimtext = geheim.encode()
    text_eingabe.delete(1.0, tk.END)
    text_eingabe.insert(tk.END, geheimtext)

def decrypt():
    geheim = Geheim(text_eingabe.get(1.0, tk.END))
    klartext = geheim.decode()
    text_eingabe.delete(1.0, tk.END)
    text_eingabe.insert(tk.END, klartext)

window = tk.Tk()
window.title("Mein geheimes Tagebuch")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

text_eingabe = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_encrypt = tk.Button(fr_buttons, text='Encrypt', command=encrypt)
btn_decrypt = tk.Button(fr_buttons, text='Decrypt', command=decrypt)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_encrypt.grid(row=3, column=0, sticky='ew', padx=5)
btn_decrypt.grid(row=4, column=0, sticky='ew', padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
text_eingabe.grid(row=0, column=1, sticky="nsew")

window.mainloop()
