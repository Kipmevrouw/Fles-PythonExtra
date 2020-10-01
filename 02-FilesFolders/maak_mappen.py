import os
bestand = open("klasgenoten.txt", "r")

tekst_regel = bestand.readline()

while tekst_regel:
    tekst_regel = tekst_regel.strip()
    print(tekst_regel)
    tekst_regel = bestand.readline()

mapnaam = ""

lengte_mapnaam = 0

while lengte_mapnaam == 0:
    mapnaam = input("Welke naam wil je voor je map van de bovenstaande namen")
    lengte_mapnaam = len(mapnaam)

    if lengte_mapnaam > 0:
        os.mkdir(mapnaam)
    else:
        print("Je hebt geen naam ingevoerd")

print("De map " + mapnaam + " is gemaakt.")

