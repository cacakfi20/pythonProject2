import tkinter as tk

def add(n):
    n += 1
    label = tk.Label(text=f"{n}")
    label.pack()

window = tk.Tk()
window.geometry("600x300")
window.title("v.1.1.")

button = tk.Button(window, text="Klikni pro přičtení", command=lambda:add(number))
button.pack()

window.mainloop()

