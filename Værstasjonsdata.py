
# Dere skal la brukeren skrive inn et årstall og så skal programmet plotte
#snødybde, nedbør, middeltemperatur og høyeste middelvind hver dag for dette året.
#Hint: Konverter datoene fra strenger til datetime objekter for å få en finere visning av
#datoene.

import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt

valgt_aarstall = int(input("Skriv inn årstall: "))
aarstall = list() 
datoer = list()
snoedybder = list() 
nedboersmengde = list()
middeltemperaturene = list()
maksimumstemperatur = list()
aller_hoyeste_middelvind = list()


filnavn = "sinnes_2014_2025_med_makstemperatur/sinnes_2014_2025_med_makstemperatur.csv"

with open(filnavn,"r",encoding = "UTF-8") as fila:

    csv_fila = csv.DictReader(fila, delimiter = ";")
    for verdier in csv_fila:
        try:
            tidspunkt = verdier["Tid(norsk normaltid)"] #Her bruker man kollonnenavnet når man lager en dict
            dato_tid = dt.strptime(tidspunkt, "%d.%m.%Y")
        except ValueError:
            print("tidspunkt error")
            continue
        
        aar =  dato_tid.year
        snoedybde = verdier["Snødybde"] #Her bruker man kollonnenavnet når man lager en dict
        snoedybde = snoedybde.replace(",", ".")
        nedboer = verdier["Nedbør (døgn)"]
        nedboer = nedboer.replace(",",".")
        middeltemperatur = verdier["Middeltemperatur (døgn)"]
        middeltemperatur = middeltemperatur.replace(",",".")
        hoyeste_middelvind = verdier["Høyeste middelvind (døgn)"]
        hoyeste_middelvind = hoyeste_middelvind.replace(",",".")
        maksimumstemperatur = verdier["Maksimumstemperatur (døgn)"]
        maksimumstemperatur = maksimumstemperatur.replace(",",".")

        if aar == valgt_aarstall:
            if "-" in (snoedybde, nedboer, middeltemperatur, hoyeste_middelvind):
                continue
            else:
                try:
                    snoedybde = float(snoedybde)
                    nedboer = float(nedboer)
                    middeltemperatur = float(middeltemperatur)
                    hoyeste_middelvind = float(hoyeste_middelvind)
                except ValueError:
                    continue
            snoedybder.append(snoedybde)
            nedboersmengde.append(nedboer)
            middeltemperaturene.append(middeltemperatur)
            aller_hoyeste_middelvind.append(hoyeste_middelvind)
            datoer.append(dato_tid)    

plt.subplot(4, 1, 1)
plt.plot(datoer, snoedybder, label="Snødybde")
plt.subplot(4, 1, 2)
plt.plot(datoer, nedboersmengde, label="Nedbør")
plt.subplot(4, 1, 3)
plt.plot(datoer, middeltemperaturene, label="Middeltemperatur")
plt.subplot(4, 1, 4)
plt.plot(datoer, aller_hoyeste_middelvind, label="Høyeste middelvind")

plt.legend()
plt.show()


