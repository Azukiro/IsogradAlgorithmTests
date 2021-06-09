# Facile - Station service - Meilleur Dev de France Octobre 2019 (Session 15:20) 
# https://www.isograd.com/FR/solutionconcours.php?cts_id=55&que_str_id=&reg_typ_id=2
Capacity = int(input())
Conso = int(input())
Station = []

for i in range(3):
    Station.append(int(input()))

Destination = int(input())

nbPlein = (Capacity / Conso) * 100
Station = sorted(Station)


CurrentPosition = 0
possible = False
for el in Station:
    if(el >= Destination):
        break
    else:
        if(CurrentPosition + nbPlein>=el):
            CurrentPosition = el
            
if(CurrentPosition + nbPlein>=Destination):
            possible = True
if possible:
    print("OK")
else:
    print("KO")