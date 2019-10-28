red = "\033[31m"
blue = "\033[34m"
N = int(input("Veuillez saisir le rang : "))
for i in range (1,N+1) :
    if(i%2==0):
        print(red,i)
    else:
        print(blue,i)