import json

with open('Daten_für_Karte.json', 'r') as routen:
    karte = json.load(routen)

def Du_zu_JSON(ort_name):
    for ort in karte:
        if ort["Name"] == ort_name:
            return ort
    print("Bitte schreibe den Namen richtig!")
    return Du_zu_JSON(ort_name)

def Weg_finden(aktuelle_position, ziel_position, aktueller_weg=[]):
    aktueller_weg = aktueller_weg + [aktuelle_position]

    if aktuelle_position == ziel_position:
        return aktueller_weg

    aktueller_ort = Position_zu_JSON(aktuelle_position)

    kuerzester_weg = None

    for nächste_position in aktueller_ort["Wohin"]:
        if nächste_position not in aktueller_weg:
            neuer_weg = Weg_finden(nächste_position, ziel_position, aktueller_weg)
            if neuer_weg:
                if kuerzester_weg is None or len(neuer_weg) < len(kuerzester_weg):
                    kuerzester_weg = neuer_weg

    return kuerzester_weg

def Position_zu_JSON(position):
    for ort in karte:
        if ort["Position"] == position:
            return ort

def main():
    anfangs_ort_name = input("Wo startest du?")
    ende_ort_name = input("Wo willst du hin?")

    anfangs_ort = Du_zu_JSON(anfangs_ort_name)
    ende_ort = Du_zu_JSON(ende_ort_name)

    kuerzester_weg = Weg_finden(anfangs_ort["Position"], ende_ort["Position"])

    if kuerzester_weg and kuerzester_weg[-1] == ende_ort["Position"]:
        print(f"Kürzester Weg von {anfangs_ort_name} nach {ende_ort_name}: {kuerzester_weg}")
        print(f"Anzahl der Stationen: {len(kuerzester_weg) - 1}")
    else:
        print(f"Es gibt keine Verbindung von {anfangs_ort_name} nach {ende_ort_name}.")

if __name__ == "__main__":
    main()
