import tkinter as tk
import customtkinter as ctk

def modern_input():

    ctk.set_appearance_mode("dark")

    root = ctk.CTk()
    root.title("Laax-input")
    root.geometry("200x400")
    root.resizable(False, False)

    options = ["1","2"]

    start = ctk.CTkOptionMenu(root, values=options)
    start.pack(pady=10, padx=10)

    ende = ctk.CTkOptionMenu(root, values=options)
    ende.pack(pady=20, padx=10)

    root.mainloop()   

modern_input()




