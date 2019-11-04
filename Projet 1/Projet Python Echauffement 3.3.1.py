import random
W = '\033[0m' #white
R = '\033[31m' #red
G = '\033[32m' #green
O = '\033[33m' #orange
B = '\033[34m' #blue
P = '\033[35m' #purple
my_colors = [W, R, G, O, B, P]
random.shuffle(my_colors)#pour ne pas tout le temps avoir la même suite de couleurs
n_colors = []
triplet = []
couleur = []

n = int(input("Combien de couleurs? (nombre limité à 6)"))
if n<=0 or n>6:
    print("ERREUR")
for i in range(0,n):
    n_colors.append(my_colors[i])
for i in range(3):
    nombre = int(input("Saisir un entier"))
    nc = random.choice(n_colors[:n])
    triplet.append(nombre)
    couleur.append(nc)

   
if((couleur[0]!=couleur[1])or(couleur[0]!=couleur[2])or(couleur[1]!=couleur[2])):
    print("Ce triplet ",'(',couleur[0],triplet[0],W,',',couleur[1],triplet[1],W,',',couleur[2],triplet[2],W,')'," n'est pas monochromatique",sep="")
else:
    print("Ce triplet ",'(',couleur[0],triplet[0],W,',',couleur[1],triplet[1],W,',',couleur[2],triplet[2],W,')'," est monochromatique",sep="")

