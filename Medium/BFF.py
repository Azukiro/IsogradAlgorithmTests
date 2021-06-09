# Easy - Classe tes amis!  #BFF - Meilleur Dev de France Octobre 2019 (Session 15:20) 
# https://www.isograd.com/FR/solutionconcours.php?cts_id=55&que_str_id=&reg_typ_id=2

N,M = input().split(" ")
N,M = int(N), int(M)
Graphe = []
for i in range(N):
    liste = []
    for j in range(N):
        liste.append(0)
    Graphe.append(liste)

for i in range(M):
    data = input().split(" ")
    p1 = int(data[0])-1
    p2 =int(data[1])-1
    Graphe[p1][p2] = 1
    Graphe[p2][p1] = 1
    
maxi = 0
current = 0
for i in range(1,N):
    counter = 0
    if(Graphe[0][i]==1):
        for j in range(N):
            if(Graphe[0][j] == 1 and Graphe[i][j]==1):
                counter +=1
        if(counter>=maxi):
            maxi = counter
            current = i
            
if(maxi < 1):
    print(-1)
else:
    print(current+1)