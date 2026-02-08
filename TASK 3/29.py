l=[]
n=int(input("Enter n:"))
for i in range(n):
    a=tuple(map(int,input().split()))
    l.append(a)
d={}
for i in l:
    d[i]=d.get(i,0)+1
print(d)

