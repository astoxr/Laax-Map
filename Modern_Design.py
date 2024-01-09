import tkinter as tk #für das Fenster
import customtkinter as ctk
from PIL import Image

def modern_design():
    ctk.set_appearance_mode("dark")

    file_path = "Laax-ski-map.jpg"

    root = ctk.CTk()
    root.title("Laax-Map")
    root.geometry("1000x521")
    root.resizable(False, False)

    karte = ctk.CTkImage(light_image=Image.open(file_path),
                    dark_image=Image.open(file_path),
                    size=(1000,521))

    image_label = ctk.CTkLabel(root, image=karte, text="")
    image_label.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)

    root.mainloop()

modern_design()