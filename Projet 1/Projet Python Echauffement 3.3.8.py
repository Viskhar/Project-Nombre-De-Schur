n=int(input("Saisir un entier à convertir"))
b=int(input("En base:"))
if n<0 or b<=1:
    print("Erreur")
quotient=b+1 #on initialise à une valeur supérieur à la base pour respecter la condition
reste=[] #la liste qui va collecter les restes

liste_diz=["A", "B", "C", "D", "E", "F"]


while quotient>=b:#car si l'on divise un nombre inférieur à 2 le nombre binaire prendera des valeurs en plus non voulu et sera faux
    quotient=n//b 
    if n%b>9:
        reste.append(liste_diz[n%b-10]) 
    else:
        reste.append(n%b)
    n=quotient  

if n>9:
    reste.append(liste_diz[n-10])
else:
    reste.append(quotient) #on prend le quotient restant qui ne peut etre divisée 
reste.reverse() #on inverse les éléments de la liste

for i in range(len(reste)): #pour afficher la liste comme un nombre
    print(reste[i], end=" ")