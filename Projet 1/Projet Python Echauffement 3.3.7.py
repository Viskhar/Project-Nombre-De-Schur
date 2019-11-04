n=int(input("Saisir un entier à convertir"))
quotient=3 #on initialise à une valeur supérieur à 2 pour respecter la condition
reste=[] #la liste qui va collecter les restes
if n<0:
    print("Erreur, l'entier doit être supérieur à 0")
    
while quotient>=2:#car si l'on divise un nombre inférieur à 2 le nombre binaire prendera des valeurs en plus non voulu et sera faux
    quotient=n//2 #q
    reste.append(n%2)
    n=quotient  

reste.append(quotient) #on ajoute le quotient restant qui ne peut etre divisée 
reste.reverse() #on inverse les éléments de la liste

for i in range(len(reste)): #pour afficher la liste comme un nombre
    print(reste[i], end=" ")


    