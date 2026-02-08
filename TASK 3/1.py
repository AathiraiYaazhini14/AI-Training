l=list(map(int,input().split()))
m=0
sm=0
for i in l:
    if i >m:
        sm=m
        m=i
print(sm)
