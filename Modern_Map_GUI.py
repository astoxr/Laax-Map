import tkinter as tk #für das Fenster
from PIL import Image, ImageTk #für Bilder einfügen
from tkinter import filedialog #für formation
import customtkinter as ctk


file_path = "Laax-ski-map.jpg"  # Das Bild wird gesucht

#das Bild wird geladen


def load_and_display_image():
    global file_path
    original_image = Image.open(file_path) #Bild öffnen

    window_width = root.winfo_width() #grösse vom Bild wird Definiert als Variabel
    window_height = root.winfo_height()

    target_size = (window_width, window_height)

    # Code um das Bild zu Formatieren
    original_image.thumbnail(target_size, Image.LANCZOS)

    #ein Label mit dem Bild wird erstellt
    photo = ImageTk.PhotoImage(original_image)
    label.configure(image=photo)
    label.image = photo  

#Grösse und Titel wird gegeben
root = ctk.CTk()
root.title("Laax-Map")
root.geometry("800x500")

#label wird erstellt
label = ctk.CTkImage(root)
label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

#def zum Laden des Bildes wird ausgeführt
root.bind("<Configure>", lambda event: load_and_display_image())


root.mainloop()
