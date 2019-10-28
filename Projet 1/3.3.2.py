p=int(input())
for a in range (1,(int(p/2)+1)):
    for b in range (a,p+1):
        if(a+b<=p):
            print('(',a,', ',b,', ',(a+b),')',sep="",end=", ")