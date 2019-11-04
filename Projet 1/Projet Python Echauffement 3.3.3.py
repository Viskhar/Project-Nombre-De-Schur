import random
R = '\033[31m' #red
B = '\033[34m' #blue
my_colors = [R, B]

verif = 0
n_colors = [0] #liste qui associe à chaque nombre de 1 à 100 une couleur (le 0 c'est pour sauter le 0)
N = int(input("Jusqu'à combien?"))

for i in range(1,N+1):#nombres possibles
    n_colors.append(my_colors[random.randint(0,1)])#couleurs attribués à la liste
for i in range(1,N+1): 
    print(n_colors[i], i, sep="", end=",")#auxquels on attribue une couleur aléatoire
print() #pour sauter une ligne 

for a in range(1,int(N/2)+1):
    for b in range(a,N):
        if(a+b<=N):
            print("(", n_colors[a],a, ",", n_colors[b], b, ",", n_colors[a+b], (a+b), ")", sep="", end=",") #va afficher a, b et a+b en couleur
            if((n_colors[a] == n_colors[b] ==  n_colors[a+b])):
                verif = 1
print()
if(verif==1):
    print("FAUX")
else:
    print("VRAI")