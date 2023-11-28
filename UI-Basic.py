# pip install Pillow

import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Laax-Map")
root.geometry("800x500")

# Load the JPG image
image_path = "Flims-Laax_pistemap.jpg"

image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.pack(padx=10, pady=10)

root.mainloop()
