import tkinter as tk #für das Fenster
from PIL import Image
import customtkinter as ctk

file_path = "Laax-ski-map.jpg"

root = ctk.CTk()
root.title("Laax-Map")
root.geometry("800x500")

karte = ctk.CTkImage(light_image=Image.open(file_path),
                   dark_image=Image.open(file_path),
                   size: Tuple[int, int] = (20, 20))

image_label = ctk.CTkLabel(root, image=karte, text="")
image_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

root.mainloop()