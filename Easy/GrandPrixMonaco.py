# Easy - Grand prix de Monaco - Meilleur Dev de France Octobre 2019 (Session 18:00) 
# https://www.isograd.com/FR/solutionconcours.php?cts_id=57&que_str_id=&reg_typ_id=2

POSITION = int(input())
N = int(input())
classement = [x for x in range(1,21)]

for x in range(N):     
    p, e = input().split(" ")     
    try:         
        p = int(p)         
        if( e == 'D') :             
            ind1 = classement.index(p)             
            ind2 = ind1 - 1             
            classement[ind1], classement[ind2] = classement[ind2], classement[ind1]                      
        else:             
            classement.remove(p)     
    except:         
        pass 
try:          
    print(classement.index(POSITION)+1) 
except:     
    print("KO")