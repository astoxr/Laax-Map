import json
# öffnen der Datei
with open('Daten_für_Karte.json', 'r') as routen:
    
    karte = json.load(routen)
# Lade die JSON-Daten


# So kannst du auf einzelne Dateien des JSON zugreiffen: print(karte[0]["Name"])


def Du_zu_JSON(ort_name):
    for ort in karte:
        if ort["Name"]== ort_name:
            ort_JSON = ort
            return(ort_JSON)
    print("Bitte schreibe den Namen richtig!")
    Du_zu_JSON(ort_name)


Anfang = input("Wo startest du?")
Anfang = Du_zu_JSON(Anfang)

Ende = input("Wo gehst du hin?")
Ende = Du_zu_JSON(Ende)

print(Anfang)
print(Ende)

def wert_aus_wohin(position,welcher):
    x=position["Wohin"]
    return(x[welcher])
print(wert_aus_wohin(Anfang,1))