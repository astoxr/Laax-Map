import tkinter as tk #für das Fenster
import customtkinter as ctk
from PIL import Image
from Programm_Karte import *

def modern_design(): #Die Map wird mit einer def Funktion gestartet, damit es eine "start.py" gibt
    ctk.set_appearance_mode("dark") #Das Design soll dunkel sein. Es passt am besten

    file_path = "Laax-ski-map.jpg"

    root = ctk.CTk()                 #hier wird der Stamm des interface's definiert auf root und verschiedene einstellungen
    root.title("Laax-Map")
    root.geometry("1200x521")
    root.resizable(False, False)

    karte = ctk.CTkImage(light_image=Image.open(file_path),    #das Bild wird hier geöffnet
                    dark_image=Image.open(file_path),
                    size=(1000,521))

    image_label = ctk.CTkLabel(root, image=karte, text="")     #hier wird es noch etwas beaurbeitet mit .pack
    image_label.pack(side="right")



    #Die Optionen für das OptionMenu werden hier definiert
    options1 = ["Von", 'Alp_Dado', 'Beginner_oben', 'Beginner_unten', 'Crap_Masegn', 'Crap_Sogn_Gion', 'Crest_la_Siala', 'Curnius', 'Falera', 'Foppa', 'Fuorcla', 'Fuorcla_da_Sagogn', 'Grauberg', 'Ils_Plauns_oben', 'Ils_Plauns_unten', 'La_Siala', 'Larnags', 'Lavadinas', 'Mutta_Rodunda', 'Nagens', 'Naraus', 'Plaun', 'Proline_Sessellift', 'Sogn_Martin', 'Stargels', 'Scansinas', 'Talstation_Flims', 'Talstation_Laax', 'Treis_Palas', 'Vorab', 'Vorab_Gletscher']
    options2 = ["Bis", 'Alp_Dado', 'Beginner_oben', 'Beginner_unten', 'Crap_Masegn', 'Crap_Sogn_Gion', 'Crest_la_Siala', 'Curnius', 'Falera', 'Foppa', 'Fuorcla', 'Fuorcla_da_Sagogn', 'Grauberg', 'Ils_Plauns_oben', 'Ils_Plauns_unten', 'La_Siala', 'Larnags', 'Lavadinas', 'Mutta_Rodunda', 'Nagens', 'Naraus', 'Plaun', 'Proline_Sessellift', 'Sogn_Martin', 'Stargels', 'Scansinas', 'Talstation_Flims', 'Talstation_Laax', 'Treis_Palas', 'Vorab', 'Vorab_Gletscher']

    #das wird ausgeführt, wenn das erste Optionmenu verändert wird
    def anf_pos(choice):
        global anfang
        anfang =  choice
        
    start = ctk.CTkOptionMenu(root, values=options1, command=anf_pos)     #hier entsteht das OptionMenu Label des "Von"
    start.pack(pady=10, padx=10)


    #das wird ausgeführt, wenn das zweite Optionmenu verändert wird
    def end_pos(choice):
        global schluss
        schluss =  choice
        
    ende = ctk.CTkOptionMenu(root, values=options2, command=end_pos)     #hier entsteht das OptionMenu Label des "Bis"
    ende.pack(pady=10, padx=10)

    

    #Das ist die Funktion, die ausgeführ wird, wenn "Suchen" geklickt wird
    #Es schickt Anfang und Schluss in den Algorythmus und bekommt die Lieste des Weges
    #Es wird wirekt auf unserem Display TextLabel dargestellt
    def pressed():
        text_d = main(anfang, schluss)
        display.configure(state="normal")
        display.delete("0.0", "end")
        for i in text_d:
            display.insert("end", i+"\n"+"\n")
        display.configure(state="disabled")

    button = ctk.CTkButton(root, text="Suchen", command=pressed)     #Der "Suchen" Button wird hier erstellt
    button.pack(pady=30, padx=10)

   
    display=ctk.CTkTextbox(root, state="disabled", border_spacing=30, height=300)     #Hier noch die TextBox für unseren Weg am Ende
    display.pack(pady=20, padx=10)

    



    root.mainloop()



