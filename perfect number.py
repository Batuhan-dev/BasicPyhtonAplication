bolenleriTopla=0
girdi=int(input(''))
for i in range(1,girdi):
    if girdi%i==0:
        print(i)
        bolenleriTopla=bolenleriTopla+i

if bolenleriTopla==girdi:
    print("perfect number")
else:
    print("not perfect number")