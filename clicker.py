import tkinter as tk


root = tk.Tk()
root.title("Игра кликер")
root.geometry("300x200")

clicks = 0

def button_click():
    global clicks
    clicks += 1
    label.config(text=f"Кликов: {clicks}")


button = tk.Button(root, text="Кликни меня!", command=button_click, bg="blue", fg="white", padx=20, pady=20, borderwidth=0, font=("Arial", 14, "bold"), width=10, height=2, relief="groove")
button.place(relx=0.5, rely=0.5, anchor="center")


label = tk.Label(root, text="Кликов: 0", font=("Arial", 12))
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


bg_button = tk.Button(root, text="Сменить фон", command=change_background, bg="white", fg="black", padx=10, pady=10, borderwidth=0, font=("Arial", 10, "bold"), relief="flat")
bg_button.place(relx=1, rely=0, anchor="ne")


root.mainloop()




