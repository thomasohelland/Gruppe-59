
# Dere skal la brukeren skrive inn et årstall og så skal programmet plotte
#snødybde, nedbør, middeltemperatur og høyeste middelvind hver dag for dette året.
#Hint: Konverter datoene fra strenger til datetime objekter for å få en finere visning av
#datoene.

import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt

with open("sinnes_2014_2025_med_makstemperatur/sinnes_2014_2025_med_makstemperatur.csv","r",encoding = "UTF-8") as fila:
    tidspunkter = list() #lager en liste for tidspunkter fra filen
    snoedybder = list() #lager en liste for akselerasjoner fra filen
    nedboer = list()
    middeltemperatur = list()
    hoyeste_middelvind = list()

    csv_fila = csv.DictReader(fila, delimiter = ";")
    for verdier in csv_fila:
        try:
            tidspunkt = verdier["Tid(norsk normaltid)"] #Her bruker man kollonnenavnet når man lager en dict
            dato_tid = dt.strptime(tidspunkt, "%d.%m.%Y")
        except ValueError as e:
            print(e)
            continue
        snoedybde = verdier["Snødybde"] #Her bruker man kollonnenavnet når man lager en dict
        tidspunkter.append(tidspunkt)
        snoedybder.append(snoedybde)


plt.plot(tidspunkter, snoedybder)
plt.xlabel("Tid(norsk normaltid)")
plt.ylabel("Snødybde")
plt.show()