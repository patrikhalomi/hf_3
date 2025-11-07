import random
from datetime import (datetime, timedelta)

def general_idojaras(filename: str):
    kezdete = datetime(2025, 10, 24)
    vege = datetime(2025, 11, 24)
    idojaras = ["szeles","napos","esős", "ködös", "normál"]

    with open(filename, "w", encoding="utf-8") as f:
        nap = kezdete
        while nap <= vege:
            ido = random.choice(idojarasok)
            homerseklet = round(random.uniform(0, 20), 1)
            eso = random.randint(0, 100)
            f.write(f"Dátum: {nap.strftime('%Y-%m-%d')}\n")
            f.write(f"Időjárás: {ido}\n")
            f.write(f"Hőmérséklet: {hom}C\n")
            f.write(f"Várható eső: {eso}%\n\n")
            nap += timedelta(days=1)

def beolvas(filename: str):

    adatok = []
    with open(fajlnev, "r", encoding="utf-8") as f:
        sorok = [sor.strip() for sor in f if sor.strip()]

        for i in range(0, len(sorok), 4):
            try:
                datum = sorok[i].split(": ")[1]
                idojaras = sorok[i + 1].split(": ")[1]
                homerseklet = float(sorok[i + 2].split(": ")[1].replace("C", ""))
                eso = int(sorok[i + 3].split(": ")[1].replace("%", ""))



