import random
W = '\033[0m' #white
R = '\033[31m' #red
G = '\033[32m' #green
O = '\033[33m' #orange
B = '\033[34m' #blue
P = '\033[35m' #purple
my_colors = [W, R, G, O, B, P]
random.shuffle(my_colors)#pour ne pas tout le temps avoir la même suite de couleurs
liste_majeure = []
liste_mineure = []
d = 1

n = int(input("Combien de couleurs? (nombre limité à 6)"))
N = int(input("Jusqu'à quel rang?"))
if N<=0 or n<=0 or n>6:
    print("ERREUR")

while d<=n**N:
    verif = 0
    while verif==0: #boucle qui va se répéter jusqu'a que l'on est utilisé toutes les couleurs demandées
        n_colors = [0]
        for i in range(1,N+1):#nombres possibles
            n_colors.append(my_colors[random.randint(0,n-1)])#on rentre les couleurs dans la liste
        for l in range(0,n-1): #on va vérifier 1 par 1 dans la liste réstrinte my_colors
            if my_colors[l] in n_colors: #si tout les élements de la liste réstreinte sont dans notre liste cela veut dire que l'on a utilisé toutes les couleurs et donc...
                verif = 1
                 
    for k in range(1,N+1):
        C = (n_colors[k], k)
        liste_mineure.append(C)
        print(liste_mineure)
    if liste_mineure not in liste_majeure:
        liste_majeure.append(liste_mineure)
        
        d = d+1
    n_colors = [0]
    liste_mineur=[]
    print() 