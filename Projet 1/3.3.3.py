import random

red = '\033[31m'
blue = '\033[34m'
black = '\033[30m'
colors = [red,blue]

N = int(input('Veuillez saisir le rang : '))

verif=0
numcolors = [0]
for i in range (1,N+1):
    numcolors.append(colors[random.randint(0,1)])
for i in range (1,N+1):
    print(numcolors[i],i,black,sep="",end=", ")
print()

for a in range (1,(int(N/2)+1)):
    for b in range (a,N+1):
        if(a+b<=N):
            print(black,'(',numcolors[a],a,black,', ',numcolors[b],b,black,', ',numcolors[a+b],(a+b),black,')',sep="",end=", ")
            if((numcolors[a]==numcolors[b])and(numcolors[a]==numcolors[a+b])):
                verif=1

print()
if(verif==1):
    print("FAUX")
else:
    print("VRAI")