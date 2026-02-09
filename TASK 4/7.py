l=list(input().split())
seen=set()
s=[]
for i in l:
    if i not in seen:
        s.append(i)
        seen.add(i)
print(s)
