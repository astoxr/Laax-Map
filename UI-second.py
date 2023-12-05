import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

file_path = "Laax-ski-map.jpg"  # Initial file path

def open_file_dialog():
    global file_path
    file_path = "Laax-ski-map.jpg"
    if file_path:
        load_and_display_image()

def load_and_display_image():
    global file_path
    # Load the image
    original_image = Image.open(file_path)

    window_width = root.winfo_width()
    window_height = root.winfo_height()

    target_size = (window_width, window_height)

    # Resize the image while maintaining its aspect ratio
    original_image.thumbnail(target_size, Image.LANCZOS)

    photo = ImageTk.PhotoImage(original_image)
    label.configure(image=photo)
    label.image = photo  

root = tk.Tk()
root.title("Laax-Map")
root.geometry("800x500")

label = tk.Label(root)
label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

root.bind("<Configure>", lambda event: load_and_display_image())

open_file_dialog()

root.mainloop()
