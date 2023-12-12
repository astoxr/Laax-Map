import json
karte_json=[
    {
        "Name":"Talstation_Laax",
        "Position":1,
        "Wohin":[2,5,3]
    },
    {
        "Name":"Larnags",
        "Position":2,
        "Wohin": [1,3]
    },
    {
        "Name":"Curnius",
        "Position":3,
        "Wohin":[2,4,5]
    },
    {
        "Name":"Falera",
        "Position":4,
        "Wohin":[3]
    },
    {
        "Name":"Crap_Sogn_Gion",
        "Position":5,
        "Wohin":[1,3,6,7,9,10]
    },
    {
        "Name":"Proline_Sessellift",
        "Position":6,
        "Wohin":[5]
    },
    {
        "Name":"Alp_Dado",
        "Position":7,
        "Wohin":[8,3]
    },
    {
        "Name":"Crest_la_Siala",
        "Position":8,
        "Wohin":[7,5,9,12,15]
    },
    {
        "Name":"Plaun",
        "Position":9,
        "Wohin":[5,22,23]
    },
    {
        "Name":"Beginner_unten",
        "Position":10,
        "Wohin":[7,11]
    },
    {
        "Name":"Beginner_oben",
        "Position":11,
        "Wohin":[5,10,7]
    },
    {
        "Name":"Treis_Palas",
        "Position":12,
        "Wohin":[7,13]
    },
    {
        "Name":"Crap_Masegn",
        "Position":13,
        "Wohin":[12,9,14,15]
    },
    {
        "Name":"Lavadinas",
        "Position":14,
        "Wohin":[16]
    },
    {
        "Name":"Fuorcla",
        "Position":15,
        "Wohin":[17,13]
    },
    {
        "Name":"Fuorcla_da_Sagogn",
        "Position":16,
        "Wohin":[15,19]
    },
    {
        "Name":"Vorab",
        "Position":17,
        "Wohin":[15,18,19,22]
    },
    {
        "Name":"Vorab_Gletscher",
        "Position":18,
        "Wohin":[17,14]
    },
    {
        "Name":"Sogn_Martin",
        "Position":19,
        "Wohin":[9,20]
    },
    {
        "Name":"La_Siala",
        "Position":20,
        "Wohin":[19,17,21,22,23,24]
    },
    {
        "Name":"Mutta_Rodunda",
        "Position":21,
        "Wohin":[19,22,24]
    },
    {
        "Name":"Scansinas",
        "Position":22,
        "Wohin":[21]
    },
    {
        "Name":"Nagens",
        "Position":23,
        "Wohin":[22,19,26]
    },
    {
        "Name":"Grauberg",
        "Position":24,
        "Wohin":[23,25]
    },
    {
        "Name":"Stargels",
        "Position":25,
        "Wohin":[24,26]
    },
    {
        "Name":"Talstation_Flims",
        "Position":26,
        "Wohin":[9]
    },
    {
        "Name":"Foppa",
        "Position":27,
        "Wohin":[26,28]
    },
    {
        "Name":"Naraus",
        "Position":28,
        "Wohin":[25,27]
    },
    {
        "Name":"Ils_Plauns_unten",
        "Position":29,
        "Wohin":[7,30,10]
    },
    {
        "Name":"Ils_Plauns_oben",
        "Position":30,
        "Wohin":[29,7,5,11,10]
    }
]
# Lade die JSON-Daten
karte = karte_json


print(karte[0]["Name"])