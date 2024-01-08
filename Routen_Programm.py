import json
# öffnen der Datei
with open('Daten_für_Karte.json', 'r') as routen:
    
    karte = json.load(routen)
# Lade die JSON-Daten

alle_wege=[]




# So kannst du auf einzelne Dateien des JSON zugreiffen: print(karte[0]["Name"])


def Du_zu_JSON(ort_name):
    for ort in karte:
        if ort["Name"]== ort_name:
            ort_JSON = ort
            return(ort_JSON)
    print("Bitte schreibe den Namen richtig!")
    Du_zu_JSON(ort_name)


#Anfang = input("Wo startest du?")
#Anfang = Du_zu_JSON(Anfang)

#Ende = input("Wo gehst du hin?")
#Ende = Du_zu_JSON(Ende)

#print(Anfang)
#print(Ende)

#Befehl um einen Bestimmten wert aus Wohin im JSON zu bekommen
def wert_aus_wohin(position,welcher):
    x=position["Wohin"]
    return(x[welcher])

#Befehl aus dem Positionswert die anderen Werte zu bekommen.
def Position_zu_JSON(Position):
    for i in karte:
        if i["Position"] == Position:
            return i

#Mit diese Befehl wird die kürzeste Verbindung zwischen zwei Orten gesucht. Mehr erklärungen folgen

def Weg_finden():
    #Hier werden die beiden Punkte, von denen man hin und her will definiert.
    Anfang = input("Wo startest du?")
    Anfang = Du_zu_JSON(Anfang)
    Ende = input("Wo willst du hin?")
    Ende = Du_zu_JSON(Ende)
    #Hier started die Suche. Es beginnt damit, dass alle verschiedenen Anfänge von Wohin vom Anfang durchgegangen werden.
    for i in Anfang["Wohin"]:
        weg = [Anfang["Position"]]
        weg.append(i)
        if i == Ende["Position"]:
            alle_wege.append(weg)
            break
        else:
            naechster_ort = Position_zu_JSON(i)
            for j in naechster_ort["Wohin"]:
                weg.append(j)
                if j == Ende["Position"]:
                    alle_wege.append(weg)
                    break
                else:
                    naechster_ort = Position_zu_JSON(j)
                    for k in naechster_ort["Wohin"]:
                        weg.append(k)
                        if k == Ende["Position"]:
                            alle_wege.append(weg)
                            break
                        else:
                             break

Weg_finden()
print(alle_wege)
            