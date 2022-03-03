import tkinter as tk
from tkinter import messagebox


def say(n):
    tk.messagebox.showinfo(
        title="Info",
        message=f"Ahoj {n}"
    )

#OKNO
window = tk.Tk()
window.geometry("600x600")
window.title("v.1.1.")

#LABEL
label_pozdrav = tk.Label(
    text="Pozdrav"
)
label_pozdrav.grid(column=0, row=0)

#ENTRY
uzivatel_entry = tk.Entry(
    width=20,
)
uzivatel_entry.grid(column=0, row=1)

#TEXT
uzivatel_text = tk.Text(
    width=20,
    height=10,
    fg="yellow",
    bg="blue"
)
uzivatel_text.grid(column=1, row=1)

#BUTTON
button = tk.Button(
    text = "Odeslat",
    width = 20,
    fg = "violet",
    command = lambda:say(uzivatel_entry.get())
)
button.grid(column=0, columnspan=100, row=4, rowspan=100, sticky="SE")

"""
konvence pro pojmenování
:
label = lbl_nazev_labelu
button = btn_nazev_labelu
entry = ent_nazev_labelu
text = txt_nazev_labelu
"""

window.mainloop()
