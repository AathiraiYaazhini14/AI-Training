m=list(map(int,input().split()))
d={'<50':[],'50-74':[],'>=75':[]}
for i in m:
    if i<50:
        d['<50'].append(i)
    elif i>=50 and i<=74:
        d['50-74'].append(i)
    else:
        d['>=75'].append(i)
print(d)
