# I. Feladat

fej_db = 0
osszes_db = 0
ketto_fej = 0

# előző két dobást tároljuk
elozo1 = ''
elozo2 = ''

with open("kiserlet.txt", "r", encoding="utf-8") as f:
    for sor in f:
        for jel in sor.strip():
            if jel not in ('F', 'I'):
                continue

            osszes_db += 1
            if jel == 'F':
                fej_db += 1

            if jel == 'I' and elozo1 == 'F' and elozo2 == 'F':
                ketto_fej += 1

            elozo2 = elozo1
            elozo1 = jel


print("A kísérlet dobásainak száma:", osszes_db)

if osszes_db > 0:
    arany = fej_db / osszes_db * 100
    print(f"A fejek aránya: {arany:.2f}%")
else:
    print("Nincs adat a fájlban.")

print("Pontosan két egymás utáni fej ennyiszer fordult elő:", ketto_fej)
