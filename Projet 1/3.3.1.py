red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
black = '\033[30m'
colors = [red,green,blue,orange,purple]
print(colors)
numcolors = [0]
n1 = int(input("Entrer l'entier souhaitée : "))
n1c= int(input("Entrer l'indice correspondant à la couleur souhaité : "))
numcolors.append(colors[n1c])
n2 = int(input("Entrer l'entier souhaitée : "))
n2c= int(input("Entrer l'indice correspondant à la couleur souhaité : "))
numcolors.append(colors[n2c])
n3 = int(input("Entrer l'entier souhaitée : "))
n3c= int(input("Entrer l'indice correspondant à la couleur souhaité : "))
numcolors.append(colors[n3c])
if((numcolors[n1]!=numcolors[n2])or(numcolors[n1]!=numcolors[n2])or(numcolors[n1]!=numcolors[n3])):
    print("Ce triplet ",'(',numcolors[n1],n1,black,',',numcolors[n2],n2,black,',',numcolors[n3],n3,black,')'," n'est pas monochromatique",sep="")
else:
    print("Ce triplet ",'(',numcolors[n1],n1,black,',',numcolors[n2],n2,black,',',numcolors[n3],n3,black,')'," est monochromatique",sep="")