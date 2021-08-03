#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

N,M = input().split(" ")
N,M = int(N), int(M)
Graphe = []
Graphe2 = []
Type = list(map(int, input().split(" ")))
for i in range(N):
    
    liste = []
    for j in range(N):
        liste.append(0)
    Graphe.append(liste)
    Graphe2.append(liste)

for i in range(M):
    data = input().split(" ")
    p1 = int(data[0])-1
    p2 =int(data[1])-1
    Graphe[p1][p2] = 1
    Graphe[p2][p1] = 1

dico = {}
dico2 = {}
for k in range(N):
    maxi = 0
    current = 0
    for i in range(N):
        if((Type[k]==0 and Type[i]==0) or (Type[k]==1 and Type[i]==1)):
            continue
        counter = 0
        for j in range(N):
            if(Graphe[k][j] == 1 and Graphe[i][j]==1):
                counter +=1
        if(counter>maxi):
            maxi = counter
            current = i
            Graphe2[k][i]=maxi
            if( not i in dico):
                dico[i]= dict()
                
            if( not k in dico):
                dico[k]= dict()
            dico[i][k]=counter
            dico[k][i]=counter
result = []
for key in dico:
    for key2 in dico[key]:
        if(dico[key])
    
