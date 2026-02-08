l=list(map(int,input().split()))
k=int(input())
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==k:
            print((i,j))

