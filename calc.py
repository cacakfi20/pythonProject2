import tkinter as tk

window = tk.Tk()
window.geometry("200x300")
window.title("Kalkulačka")

ent = tk.Entry(
    width=20,
    bg="grey",
    fg="white"
)
ent.insert(1, 0)
ent.grid(column=0, row=0, sticky="W", columnspan= 4)

btn_AC = tk.Button(
    text="AC",
    width=5,
    height=3,
    bg="dark grey"
)
btn_AC.grid(column=0, row=1, sticky="W")

btn_couz = tk.Button(
    text="+/-",
    width=5,
    height=3,
    bg="dark grey"
)
btn_couz.grid(column=1, row=1, sticky="W")

btn_procento = tk.Button(
    text="%",
    width=5,
    height=3,
    bg="dark grey"
)
btn_procento.grid(column=2, row=1, sticky="W")

btn_deleno = tk.Button(
    text="/",
    width=5,
    height=3,
    bg="dark grey"
)
btn_deleno.grid(column=3, row=1, sticky="W")

btn_7 = tk.Button(
    text="7",
    width=5,
    height=3,
    bg="dark grey"
)
btn_7.grid(column=0, row=2, sticky="W")

btn_8 = tk.Button(
    text="8",
    width=5,
    height=3,
    bg="dark grey"
)
btn_8.grid(column=1, row=2, sticky="W")

btn_9 = tk.Button(
    text="9",
    width=5,
    height=3,
    bg="dark grey"
)
btn_9.grid(column=2, row=2, sticky="W")

btn_krat = tk.Button(
    text="X",
    width=5,
    height=3,
    bg="dark grey"
)
btn_krat.grid(column=3, row=2, sticky="W")

btn_4 = tk.Button(
    text="4",
    width=5,
    height=3,
    bg="dark grey"
)
btn_4.grid(column=0, row=3, sticky="W")

btn_5 = tk.Button(
    text="5",
    width=5,
    height=3,
    bg="dark grey"
)
btn_5.grid(column=1, row=3, sticky="W")

btn_6 = tk.Button(
    text="6",
    width=5,
    height=3,
    bg="dark grey"
)
btn_6.grid(column=2, row=3, sticky="W")

btn_minus = tk.Button(
    text="-",
    width=5,
    height=3,
    bg="dark grey"
)
btn_minus.grid(column=3, row=3, sticky="W")

btn_1 = tk.Button(
    text="1",
    width=5,
    height=3,
    bg="dark grey"
)
btn_1.grid(column=0, row=4, sticky="W")

btn_2 = tk.Button(
    text="2",
    width=5,
    height=3,
    bg="dark grey"
)
btn_2.grid(column=1, row=4, sticky="W")

btn_3 = tk.Button(
    text="3",
    width=5,
    height=3,
    bg="dark grey"
)
btn_3.grid(column=2, row=4, sticky="W")

btn_plus = tk.Button(
    text="+",
    width=5,
    height=3,
    bg="dark grey"
)
btn_plus.grid(column=3, row=4, sticky="W")

btn_0 = tk.Button(
    text="0",
    width=11,
    height=3,
    bg="dark grey"
)
btn_0.grid(column=0, columnspan=2, row=5, sticky="W")

btn_carka = tk.Button(
    text=",",
    width=5,
    height=3,
    bg="dark grey"
)
btn_carka.grid(column=2, row=5, sticky="W")

btn_rovnitko = tk.Button(
    text="=",
    width=5,
    height=3,
    bg="dark grey"
)
btn_rovnitko.grid(column=3, row=5, sticky="W")


window.mainloop()