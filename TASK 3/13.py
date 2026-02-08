tup=[(1,2), (2,1), (3,4)]
seen=set()
final=[]
for a,b in tup:
    key=tuple(sorted((a,b)))
    if key not in seen:
        seen.add(key)
        final.append(key)
print(final)
