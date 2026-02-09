tr= [
    [20, 30, 25, 40],
    [35, 45, 30, 20],
    [50, 20, 40, 30]
]
m=0
mi=[]
mh=0
mhi=0
for i in tr:
    if sum(i)>m:
        m=sum(i)
        mi=i
    for j in i:
        if j>mh:
            mh=j
print(mi)
print(mh)
