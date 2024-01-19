import json
from Modern_Design import *


#Hier laden wir JSON Datei, so dass wir damit arbeiten können.
with open('Daten_für_Karte.json', 'r') as routen:
    karte = json.load(routen)


#Modularer Entwurf um von der JSON Datei aus dem Namen die anderen Infos zu bekommen.
def Du_zu_JSON(ort_name):
    for ort in karte:
        if ort["Name"] == ort_name:
            return ort
    print("Bitte schreibe den Namen richtig!")
    return Du_zu_JSON(ort_name)

#Befehl um Weg zu finden
def Weg_finden(aktuelle_position, ziel_position, aktueller_weg=[]):
    aktueller_weg = aktueller_weg + [aktuelle_position] #Der aktuelle Weg wird ergänzt

    if aktuelle_position == ziel_position:
        return aktueller_weg #In diesem Befehl gibt es eine Schlaufe, diese wird heir beendet, sobald die Endposition erreicht wird.

    aktueller_ort = Position_zu_JSON(aktuelle_position) #Modularer entwurf von unten wird gebraucht

    kuerzester_weg = None #Die Variabel kürzester Weg wird hinzugefügt, welche später gebraucht wird.

    for nächste_position in aktueller_ort["Wohin"]: #Hier werden alle Positionen, in die man von dem aktuellen Ort gehen kann, abgearbeitet
        if nächste_position not in aktueller_weg: #Hier wird geprüft, ob die Position schon einmal im Weg war, um Schlaufen zu vermeiden
            neuer_weg = Weg_finden(nächste_position, ziel_position, aktueller_weg) #Der Befehl ruft sich selbst wieder auf um den Weg zu ergänzen
            if neuer_weg:
                if kuerzester_weg is None or len(neuer_weg) < len(kuerzester_weg): #Hier wird deiser Weg mit dem alten abgeglichen um den kürzesten zu finden.
                    kuerzester_weg = neuer_weg
#Bei diesem gesamten letzten absatz geht es darum, dass die verscheidenen Wohins abgesucht werden und dann wieder in den Befehl nochmals
#eingefügt werden. Diese Schlaufe wiederholt sich, bis entweder der das Ziel erreicht wird oder der weg in einer Schlaufe ist.

    return kuerzester_weg

#Modularer Befehl um alle Daten der JSON Datei aus der Position zu bekomme.
def Position_zu_JSON(position):
    for ort in karte:
        if ort["Position"] == position:
            return ort

kuerzester_weg_Namen=[]

def main(anfangs_ort_name,ende_ort_name):
    kuerzester_weg_Namen=[]
    

    anfangs_ort = Du_zu_JSON(anfangs_ort_name)
    ende_ort = Du_zu_JSON(ende_ort_name) #Hier wird mit den Modularen Befehlen von vorher der Input gesucht und dann gerade in JSON format umgewandelt.

    kuerzester_weg = Weg_finden(anfangs_ort["Position"], ende_ort["Position"]) #Mit dem Befehl "Weg_finden" wird der kürzeste Weg gesucht.

    if kuerzester_weg and kuerzester_weg[-1] == ende_ort["Position"]:
        
        for i in kuerzester_weg:
            i= Position_zu_JSON(i)
            kuerzester_weg_Namen.append(i["Name"])
        print(kuerzester_weg_Namen) #Hier wird der Weg aus Zahlen zu den Namen umgeschrieben für einfacheres Verständnis.
        return kuerzester_weg_Namen
    else:
        print(f"Es gibt keine Verbindung von {anfangs_ort_name} nach {ende_ort_name}.") #Hier wird noch überprüft, ob es eine Verbindung gibt.
    


