data=list(map(int,input().split()))
rl=list(map(int,input().split()))
for i in rl:
    if i in data:
        data.remove(i)
print(data)
