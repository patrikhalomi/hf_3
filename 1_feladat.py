import random
import math
import datetime
import statistics

# Mai dátum
napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
ma = datetime.date.today()
het_napja = napok[ma.weekday()]
ev_napja = ma.timetuple().tm_yday

print("Mai dátum:", ma)
print("A hét napja:", het_napja)
print("Az év", ev_napja, ". napja")

#  számok generálása 1 és 100 között
szamok = []
for i in range(10):
    szam = random.randint(1, 100)
    szamok.append(szam)

print("Generált számok:", szamok)

# Véletlenszerű
szerencseszam = random.choice(szamok)
print("Szerencseszám:", szerencseszam)

# Statisztikai értékek
atlag = statistics.mean(szamok)
szoras = statistics.stdev(szamok)
maximum = max(szamok)
minimum = min(szamok)
osszeg = sum(szamok)
gyok = math.sqrt(osszeg)

print("Átlag:", atlag)
print("Szórás:", szoras)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Összeg gyöke:", gyok)

# Prímszám ellenőrzés
def prim(szam):
    if szam < 2:
        return False
    for i in range(2, int(math.sqrt(szam)) + 1):
        if szam % i == 0:
            return False
    return True

if prim(szerencseszam):
    print(" prímszám.")
else:
    print(" nem prímszám.")
