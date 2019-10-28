convert=[]
convertinv=[]
Convertisseur=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nombre=float(input("Quel est le nombre que vous voulez convertir ? : "))
base=int(input("En quel base voulez vous la convertir ? : "))
precision=0
precisionbase=0
precision10=-1
if(nombre==int(nombre)):
    dividende=nombre
    while(dividende!=0):
        convert.append(int(dividende-base*(int(dividende/base))))
        dividende=int(dividende/base)
    for cmp in range(0,len(convert)):
        cmpinv=len(convert)-cmp-1
        convertinv.append(convert[cmpinv])
else:
    dividende=int(nombre)
    while(dividende!=0):
        convert.append(int(dividende-base*(int(dividende/base))))
        dividende=int(dividende/base)
    for cmp in range(0,len(convert)):
        cmpinv=len(convert)-cmp-1
        convertinv.append(convert[cmpinv])
    convertinv.append(',')
    decimal=nombre-int(nombre)
    precision10=decimal
    while(int(precision10)!=precision10):
        precision10=precision10*10
        precision=precision+1
    while(precision-base**precisionbase>0):
        precisionbase=precisionbase+1
    for cmp in range(0,precisionbase):
        decimal=decimal*base
        if(decimal>=1):
            convertinv.append(int(decimal))
            decimal=decimal-int(decimal)
        else:
            convertinv.append(0)

print('[',end=' ')
for cmp in range(0,len(convertinv)):
    if(convertinv[cmp]==','):
        print(', ',end='')
    else:
        if(base<=36):
            print(Convertisseur[convertinv[cmp]],end=' ')
        else:
            print(convertinv[cmp],end=' ')
print("] est le nombre en base",base,"de",nombre)