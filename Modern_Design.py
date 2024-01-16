import tkinter as tk #für das Fenster
import customtkinter as ctk
from PIL import Image

def modern_design():
    ctk.set_appearance_mode("dark")

    file_path = "Laax-ski-map.jpg"

    root = ctk.CTk()
    root.title("Laax-Map")
    root.geometry("1200x521")
    root.resizable(False, False)

    karte = ctk.CTkImage(light_image=Image.open(file_path),
                    dark_image=Image.open(file_path),
                    size=(1000,521))

    image_label = ctk.CTkLabel(root, image=karte, text="")
    image_label.pack(side="right")




    options = ['Talstation_Laax', 'Larnags', 'Curnius', 'Falera', 'Crap_Sogn_Gion', 'Proline_Sessellift', 'Alp_Dado', 'Crest_la_Siala', 'Plaun', 'Beginner_unten', 'Beginner_oben', 'Treis_Palas', 'Crap_Masegn', 'Lavadinas', 'Fuorcla', 'Fuorcla_da_Sagogn', 'Vorab', 'Vorab_Gletscher', 'Sogn_Martin', 'La_Siala', 'Mutta_Rodunda', 'Scansinas', 'Nagens', 'Grauberg', 'Stargels', 'Talstation_Flims', 'Foppa', 'Naraus', 'Ils_Plauns_unten', 'Ils_Plauns_oben']

    start = ctk.CTkOptionMenu(root, values=options)
    start.pack(pady=10, padx=10)


    ende = ctk.CTkOptionMenu(root, values=options)
    ende.pack(pady=20, padx=10)



    root.mainloop()
    

modern_design()