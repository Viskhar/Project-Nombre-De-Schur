convert=[]
nombre=float(input("Quel est le nombre que vous voulez convertir ? : "))
reel=nombre
precisionbase=-1
precision=0
puiss=0
verif=0
if(nombre==int(nombre)):
    for cmp in range (0,int(nombre/2)+1):
        puiss=int(nombre/2)-cmp
        if(reel-2**puiss>=0):
            convert.append(1)
            reel=reel-2**puiss
            verif=1
        elif(verif==1):
            convert.append(0)
else:
    reel=int(nombre)
    decimal=nombre-int(nombre)
    for cmp in range (0,int(nombre/2)+1):
        puiss=int(nombre/2)-cmp
        if(reel-2**puiss>=0):
            convert.append(1)
            reel=reel-2**puiss
            verif=1
        elif(verif==1):
            convert.append(0)
    convert.append(',')
    precision10=decimal
    while(int(precision10)!=precision10):
        precision10=precision10*10
        precision=precision+1
    while(precision-2**precisionbase>0):
        precisionbase=precisionbase+1
    for cmp in range(0,precisionbase):
        decimal=decimal*2
        if(decimal>=1):
            decimal=decimal-1
            convert.append(1)
        else:
            convert.append(0)

print("[",end=" ")
for cmp in range(0,len(convert)):
    if(convert[cmp]==','):
        print(' , ',end="")
    else:
        print(convert[cmp],end="")
print(" ] est le nombre binaire de",nombre)