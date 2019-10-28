import random

red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
black = '\033[30m'
colors = [red,green,blue,orange,purple]

N = int(input('Veuillez saisir le rang : '))
n = int(input("Entrer le nombre de couleur à utiliser (Max 5) : "))
colorsn=colors[:n]

verif=0
numcolors = [0]
for i in range (1,N+1):
    numcolors.append(colorsn[random.randint(0,n-1)])
for i in range (1,N+1):
    print(numcolors[i],i,sep="",end=", ")
print()

v2=0
for i in colorsn:
    v=0
    for j in numcolors:
        if((i==j)and(v==0)):
            v2=v2+1
            v=1
if(v2==len(colorsn)):
    print(black,"VRAI")
else:
    print(black,"FAUX")