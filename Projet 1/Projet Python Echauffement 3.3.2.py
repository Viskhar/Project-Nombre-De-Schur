import random

p = int(input("Jusqu'à combien?"))

if p>100:
    print("ERREUR. Saisir un entier positif et inférieur à 100")

for i in range(1,p+1):
    print(i, sep="", end=",")
print() #pour sauter une ligne 

for a in range(1,int(p/2)+1):
    for b in range(a, p):
        if(a+b<=p):
            print("(", a, ",",  b, ",", (a+b), ")", sep="", end=",") #va afficher a, b et a+b 
            