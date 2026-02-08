n=list(map(int,input().split()))
ml=1
l=1
for i in range(len(n)-1):
    if n[i+1]-n[i]==1:
        l+=1
    else:
        l=1
    ml=max(ml,l)
print(ml)
