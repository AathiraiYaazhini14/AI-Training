l=[]
pe={}
n=int(input())
for i in range(n):
    pid=int(input())
    ear=int(input())
    l.append((pid,ear))
print(l)
for i in l:
    pe[i[0]]=pe.get(i[0],0)+i[1]
print(pe)
m=0
par=0
for i in pe:
    pe[i]/=len(pe)
    if m<pe[i]:
        m=pe[i]
        par=i
print(par,':',m)
