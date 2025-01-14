from email.policy import default
from tkinter import *

root = Tk()
root.title("Заголовок вікна")
root.geometry("500x500+430+100")
root.iconbitmap(default="skull_and_bones_halloween_23219.ico")

label = Label(text="Привіт! вам всім треба більше працювати")
label.pack()

root.mainloop()