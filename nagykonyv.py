f = open("./konyvek.txt", "r", encoding="utf-8")
#print(f.read())
#print(f.readlines())

for sor in f:
    print(sor)

f.close()


konyvek = []
with open('./konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = adatok[0]
        szul_ev = int(adatok[1])
        if adatok[2]:
            hal_ev = int(adatok[2])
        else:
            hal_ev = None
        nemzetiseg = adatok[3]
        cim = adatok[4]
        helyezes = adatok[5]
#        konyv = {'nev': adatok[0], 'szulEv': int(adatok[1]), 'halEv': adatok[2], 'nemzetiseg': adatok[3], 'cim': adatok[4], 'helyezes': adatok[5]}
#        konyvek.append(konyv)
        konyvek.append([nev, szul_ev, hal_ev, nemzetiseg, cim, helyezes])

#print(f'{konyvek=}')
print(f'3.2 feladat: Az állományban {len(konyvek)} db könyv adatai szerepelnek.')

legjobb_konyv = None
for konyv in konyvek:
    if konyv[3] == 'magyar':
        if legjobb_konyv is None or konyv[5] < legjobb_konyv[5]:
            legjobb_konyv = konyv

print(f'3.3 feladat: A legjobb helyezést elért magyar {legjobb_konyv[0]}: {legjobb_konyv[4]}' )