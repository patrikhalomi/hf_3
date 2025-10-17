import datetime

honap = int(input("Add meg a születésnap hónapját (1-12): "))
nap = int(input("Add meg a születésnap napját (1-31): "))

# lekérdezés
ma = datetime.date.today()
ev = ma.year

kovetkezo_szuletesnap = datetime.date(ev, honap, nap)

if kovetkezo_szuletesnap < ma:
    kovetkezo_szuletesnap = datetime.date(ev + 1, honap, nap)

kulonbseg = kovetkezo_szuletesnap - ma
print("A következő születésnapodig még", kulonbseg.days, "nap van.")
