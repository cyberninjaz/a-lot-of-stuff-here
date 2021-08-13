import tkinter as tk
from tkinter.constants import S

thing = None

window = tk.Tk()

img = tk.PhotoImage(file="troll.png")


photo = tk.PhotoImage(file="error.png")

button = tk.Button(
    master=window,
    text="LAUNCH",
    font=("Airborne", 64),
    width=25,
    height=5,
    bg="black",
    fg="red",
)

def onClick(event):
    for i in range(100):
        w = tk.Toplevel(master=window)
        lbl = tk.Label(master=w, image=img)
        lbl.pack()
    
    def onEntry(event):
        for i in range(100):
            w = tk.Toplevel(master=window)
            lbl = tk.Label(master=w, image=photo)
            lbl.pack()

    def onSubmit(event):
        global thing
        thing = entry.get()
        if thing == "Hello":
            entry.bind("<Return>", onEntry)

    w = tk.Toplevel()

    label = tk.Label(master=w, text="Password: Hello", font=("Arial", 64))
    label.pack()

    label = tk.Label(master=w, text="Enter Password:")
    entry = tk.Entry(master=w, font=("Arial", 64))
    label.pack()
    entry.pack()

    entry.bind("<Return>", onSubmit)

button.bind("<Button>", onClick)
button.pack()

window.mainloop()

def on_closing():
    pass

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()