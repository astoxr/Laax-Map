import json
# öffnen der Datei
with open('Daten_für_Karte.json', 'r') as routen:
    
    karte = json.load(routen)
# Lade die JSON-Daten


# So kannst du auf einzelne Dateien des JSON zugreiffen: print(karte[0]["Name"])


def Du_zu_JSON(du):
    for ort in karte:
        if ort["Name"]==du:
            ort_JSON = ort
            return(ort_JSON)
    print("Bitte schreibe den Namen richtig!")
print(Du_zu_JSON("Nagens"))

