import random
N = int(input('Veuillez saisir le rang : '))
n = int(input("Veuillez saisir le nombre de couleur (Max 5) : "))
red = "\033[31m"
blue = "\033[34m"
green = "\033[32m"
orange = "\033[33m"
purple = "\033[35m"
colors = [red, blue, green, orange, purple]
colorsn = colors[:n]
randblue=0
randred=0
randgreen=0
randorange=0
randpurple=0

for i in range (1,N+1):
    rand = random.choice(colorsn)
    if(rand==blue):
        randblue=randblue+1
        if(randblue>(N/n)):
            colorsn.remove(rand)
            rand=random.choice(colorsn)
            n=n-1
    elif(rand==red):
        randred=randred+1
        if(randred>(N/n)):
            colorsn.remove(rand)
            rand=random.choice(colorsn)
            n=n-1
    elif(rand==green):
        randgreen=randgreen+1
        if(randgreen>(N/n)):
            colorsn.remove(rand)
            rand=random.choice(colorsn)
            n=n-1
    elif(rand==orange):
        randorange=randorange+1
        if(randorange>(N/n)):
            colorsn.remove(rand)
            rand=random.choice(colorsn)
            n=n-1
    elif(rand==purple):
        randpurple=randpurple+1
        if(randpurple>(N/n)):
            colorsn.remove(rand)
            rand=random.choice(colorsn)
            n=n-1
    print(rand,i)