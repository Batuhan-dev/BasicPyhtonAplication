sayac=1
girdi=int(input(''))

while girdi!=1:
    sayac=sayac+1
    if girdi%2==0:
        girdi=girdi/2
    else:
        girdi=(3*girdi)+1
    

print(sayac)