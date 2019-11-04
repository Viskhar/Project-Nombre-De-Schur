import random
W = '\033[0m' #white
R = '\033[31m' #red
G = '\033[32m' #green
O = '\033[33m' #orange
B = '\033[34m' #blue
P = '\033[35m' #purple

print("Nombres de termes?")
N = int(input())  #les premiers nombres
print("Nombre de couleurs(inférieur à 7)")
n = int(input())

my_color = [W, R, G, O, B, P]
random.shuffle(my_color)

for i in range(1, N+1):
    print(random.choice(my_color[:n]), i, end=',') #la liste prend un nombre i allant de 1 à N+1 de couleur aléatoire parmi les couleurs choisis
