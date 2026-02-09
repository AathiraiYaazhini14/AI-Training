orders = ["Pizza", "Burger", "Pizza", "Pasta", "Burger", "Pizza"]
freq={}
for i in orders:
    freq[i]=freq.get(i,0)+1
f=sorted(freq,key=lambda x:freq[x],reverse=True)
print(f[0])
for i in freq:
    if freq[i]==1:
        print(i)
