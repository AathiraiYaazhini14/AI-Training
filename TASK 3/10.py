n=list(input().split())
m=list(map(int,input().split()))
comb=dict(zip(n,m))
sc=dict(sorted(comb.items(),key=lambda x:x[1],reverse=True))
for i,value in enumerate(sc,1):
    print(i,':',value)
    
