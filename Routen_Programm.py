import json
# öffnen der Datei
with open('Daten_für_Karte.json', 'r') as routen:
    
    karte = json.load(routen)
# Lade die JSON-Daten


# So kannst du auf einzelne Dateien des JSON zugreiffen: print(karte[0]["Name"])

def Du_zu_JSON(du):
    du=input("Wo bist du?")
    for i in len(karte):
        if karte[i]["Name"]==du:
            du = karte[i]
            return(du)
            break
Du_zu_JSON