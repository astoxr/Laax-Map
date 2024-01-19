import tkinter as tk #für das Fenster
import customtkinter as ctk
from PIL import Image
from Programm_Karte import *

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




    options1 = ['Von',' Talstation_Laax', 'Larnags', 'Curnius', 'Falera', 'Crap_Sogn_Gion', 'Proline_Sessellift', 'Alp_Dado', 'Crest_la_Siala', 'Plaun', 'Beginner_unten', 'Beginner_oben', 'Treis_Palas', 'Crap_Masegn', 'Lavadinas', 'Fuorcla', 'Fuorcla_da_Sagogn', 'Vorab', 'Vorab_Gletscher', 'Sogn_Martin', 'La_Siala', 'Mutta_Rodunda', 'Scansinas', 'Nagens', 'Grauberg', 'Stargels', 'Talstation_Flims', 'Foppa', 'Naraus', 'Ils_Plauns_unten', 'Ils_Plauns_oben']
    options2 = ['Bis', 'Talstation_Laax', 'Larnags', 'Curnius', 'Falera', 'Crap_Sogn_Gion', 'Proline_Sessellift', 'Alp_Dado', 'Crest_la_Siala', 'Plaun', 'Beginner_unten', 'Beginner_oben', 'Treis_Palas', 'Crap_Masegn', 'Lavadinas', 'Fuorcla', 'Fuorcla_da_Sagogn', 'Vorab', 'Vorab_Gletscher', 'Sogn_Martin', 'La_Siala', 'Mutta_Rodunda', 'Scansinas', 'Nagens', 'Grauberg', 'Stargels', 'Talstation_Flims', 'Foppa', 'Naraus', 'Ils_Plauns_unten', 'Ils_Plauns_oben']


    def anf_pos(choice):
        global anfang
        anfang =  choice
        
    start = ctk.CTkOptionMenu(root, values=options1, command=anf_pos)
    start.pack(pady=10, padx=10)



    def end_pos(choice):
        global schluss
        schluss =  choice
        
    ende = ctk.CTkOptionMenu(root, values=options2, command=end_pos)
    ende.pack(pady=10, padx=10)

    
    #print(anfang, schluss)
    #main(anfang, schluss)

    def pressed():
        text_d = main(anfang, schluss)
        display.configure(state="normal")
        display.delete("0.0", "end")
        for i in text_d:
            display.insert("end", i+"\n"+"\n")
        display.configure(state="disabled")

    button = ctk.CTkButton(root, text="Search", command=pressed)
    button.pack(pady=30, padx=10)

   
    display=ctk.CTkTextbox(root, state="disabled", border_spacing=30, height=300)
    display.pack(pady=20, padx=10)

    



    root.mainloop()



