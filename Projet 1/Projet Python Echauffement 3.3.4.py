import random
W = '\033[0m' #white
R = '\033[31m' #red
G = '\033[32m' #green
O = '\033[33m' #orange
B = '\033[34m' #blue
P = '\033[35m' #purple
my_colors = [W, R, G, O, B, P]
random.shuffle(my_colors)#pour ne pas tout le temps avoir la même suite de couleur
n_colors = [0]

verif = 0
n = int(input("Combien de couleurs? (nombre limité à 6)"))
N = int(input("Jusqu'à quel rang?"))
if N<=0 or n<=0 or n>6:
    print("ERREUR")

for i in range(1,N+1):#nombres possibles
    n_colors.append(my_colors[random.randint(0,n-1)])#on rentre les couleurs dans la liste
for i in range(0,n-1): #on va vérifier 1 par 1 dans la liste réstreinte my_colors
    if my_colors[i] not in n_colors: #si un élement de la liste réstreinte n'est pas dans notre liste...
        verif = 1
for i in range(1,N+1): 
    print(n_colors[i], i, sep="", end=",")#on attribue à un nombre i une couleur aléatoire
print() #pour sauter une ligne 

for a in range(1,int(N/2)+1):
    for b in range(a, N-1):
        if(a+b<=N):
            print("(", n_colors[a],a, ",", n_colors[b], b, ",", n_colors[a+b], (a+b), ")", sep="", end=",") #va afficher a, b et a+b en couleur
           
print()
if(verif==1):
    print("FAUX")
else:
    print("VRAI")