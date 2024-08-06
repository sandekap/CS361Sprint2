import tkinter as tk
from tkinter import simpledialog

user_alert = []
while len(user_alert)<=0:
    file = open("users.txt", 'r')
    users = file.readline()
    if users is not None:
        file.close()
        root = tk.Tk()
        root.withdraw()

        user_input = simpledialog.askstring("Input", "When is your pet due for their next vaccines?")
        file = open("button.txt", 'w')
        file.write("Do Not Forget to Schedule your Pets vaccination by the following date:")
        file.write(user_input)
        file.close()
        print("Reminder schedule your pet for their next vaccinations before:", user_input)

        root.mainloop()

    else:
        print("There are no registered users yet, please register before setting your alert")