def calculation(l):
    mi=min(l)
    ma=max(l)
    avg=sum(l)/len(l)
    return((mi,ma,avg))
l=[1,2,3,4,5]
print(calculation(l))
