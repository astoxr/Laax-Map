import json
# öffnen der Datei
with open('Daten_für_Karte.json', 'r') as routen:
    
    karte = json.load(routen)



def Hallo():
    print("hallo")
Hallo()