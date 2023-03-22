import tkinter as tk


root = tk.Tk()
root.title("Игра кликер")


clicks = 0

def button_click():
    global clicks
    clicks += 1
    label.config(text=f"Кликов: {clicks}")


button = tk.Button(root, text="Кликни меня!", command=button_click)
button.pack()


label = tk.Label(root, text="Кликов: 0")
label.pack()


current_bg = "white"


def change_background():
    global current_bg
    if current_bg == "white":
        root.configure(background="black")
        current_bg = "black"
    else:
        root.configure(background="white")
        current_bg = "white"


bg_button = tk.Button(root, text="Сменить фон", command=change_background)
bg_button.pack()


root.mainloop()

