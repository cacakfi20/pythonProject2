import tkinter as tk

number = [0]
def add(n):
    n.append(n[-1] + 1)
    label = tk.Label(text=f"{n[-1]}")
    label.pack()

window = tk.Tk()
window.geometry("600x300")
window.title("v.1.1.")

button = tk.Button(
    text = "Klikni pro přičtení",
    width = 20,
    height = 5,
    fg = "violet",
    command = lambda:add(number)
)
button.pack()

uzivatel_entry = tk.Entry(
    width=20,

)
uzivatel_entry.pack()

window.mainloop()
