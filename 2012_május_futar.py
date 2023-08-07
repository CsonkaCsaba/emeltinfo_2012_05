# 1. feladat

print("2. feladat")
utak=[]

with open ("tavok.txt", "r") as forras:
    
# 2. feladat

    for k in forras:
        ut = k.split()
        utak.append([int(ut[0]),int(ut[1]),int(ut[2])])
        
for ut in utak:
    if  ut[0] == 1 and ut[1] == 1:
        print(f"Heti első fuvar megtett távolsága: {ut[2]} km.")
        
    elif ut[0] == 2 and ut[1] == 1:
        print(f"Heti első fuvar megtett távolsága: {ut[2]} km.")
        
    elif ut[0] == 3 and ut[1] == 1:
        print(f"Heti első fuvar megtett távolsága: {ut[2]} km.")
        
    elif ut[0] == 4 and ut[1] == 1:
        print(f"Heti első fuvar megtett távolsága: {ut[2]} km.")
        
    elif ut[0] == 5 and ut[1] == 1:
        print(f"Heti első fuvar megtett távolsága: {ut[2]} km.")
        
    elif ut[0] == 6 and ut[1] == 1:
        print(f"Heti első fuvar megtett távolsága: {ut[2]} km.")
        
    elif ut[0] == 7 and ut[1] == 1:
        print(f"Heti első fuvar megtett távolsága: {ut[2]} km.")
        

# 3. feladat

print("3. feladat")

utolso_ut=[]
for ut in utak:
        if ut[0] == 7 and ut[1] > ut[1-1]:
            z=ut[2]
            utolso_ut.append(z)
            
print(f"Az utolsó nap utolsó fuvarának távolsága: {utolso_ut[0]} km.")

# 4. feladat

print("4. feladat")
munkanapok=[]

for ut in utak:
    munkanapok.append(ut[0])
    
munkanapok=list(dict.fromkeys(munkanapok))

napok=[1,2,3,4,5,6,7]
szabadnapok=[]

for n in napok:
    if n in munkanapok:
        continue
    else:
        szabadnapok.append(n)
        
print(f"Szabadnap a hét {szabadnapok[0]}. napja, és a hét {szabadnapok[1]} napja.")

# 5. feladat

print("5. feladat")
legtobbfuvar=[0,0,0]
utak.sort()
y=0
for ut in utak:
    x=ut[1]
    if x > y:
        y=x
        z=ut[0]
print(f"A hét {z}. napján volt a legtöbb fuvar.")

# 6. feladat

print("6. feladat")
elso=[]
masodik=[]
harmadik=[]
negyedik=[]
otodik=[]
hatodik=[]
hetedik=[]

for ut in utak:
    if ut[0] == 1:
        elso.append(ut[2])
    if ut[0] == 2:
        masodik.append(ut[2])
    if ut[0] == 3:
        harmadik.append(ut[2])
    if ut[0] == 4:
        negyedik.append(ut[2])
    if ut[0] == 5:
        otodik.append(ut[2])
    if ut[0] == 6:
        hatodik.append(ut[2])
    if ut[0] == 7:
        hetedik.append(ut[2])
        
print(f"1. nap: {sum(elso)} km")
print(f"2. nap: {sum(masodik)} km")
print(f"3. nap: {sum(harmadik)} km")
print(f"4. nap: {sum(negyedik)} km")
print(f"5. nap: {sum(otodik)} km")
print(f"6. nap: {sum(hatodik)} km")
print(f"7. nap: {sum(hetedik)} km")

# 7. feladat

print("7. feladat")
szam = int(input("Adja meg a távolságot: "))
if szam >= 1 and szam <= 2:
    print("500 Ft")
if szam >= 3 and szam <= 5:
    print("700 Ft")
if szam >= 6 and szam <= 10:
    print("900 Ft")
if szam >= 11 and szam <= 20:
    print("1 400 Ft")
if szam >= 21 and szam <= 30:
    print("2 000 Ft")

# 8. feladat

print("8. feladat")
utak.sort()
with open ("dijazas.txt", "x", encoding="utf-8") as dijazas:
    for ut in utak:
        if ut[2] >= 1 and szam <= 2:
            print(f"{ut[0]}. nap {ut[1]}. út: 500 Ft", file=dijazas)
        if ut[2] >= 3 and szam <= 5:
            print(f"{ut[0]}. nap {ut[1]}. út: 700 Ft", file=dijazas)
        if ut[2] >= 6 and szam <= 10:
            print(f"{ut[0]}. nap {ut[1]}. út: 900 Ft", file=dijazas)
        if ut[2] >= 11 and szam <= 20:
            print(f"{ut[0]}. nap {ut[1]}. út: 1400 Ft", file=dijazas)
        if ut[2] >= 21 and szam <= 30:
            print(f"{ut[0]}. nap {ut[1]}. út: 2000 Ft", file=dijazas)

# 9. feladat
osszegek=[]
with open ("dijazas.txt", "r", encoding="utf-8") as penzek:
    for a in penzek:
        penz=a.split()
        osszegek.append(int(penz[-2]))
fizetes= 0
for osszeg in osszegek:
    fizetes=fizetes+osszeg
print(f"Heti fizetés: {fizetes} Ft")