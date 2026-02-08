l=list(input().split())
d={}
for i in l:
    if len(i) in d:
        d[len(i)].append(i)
    else:
        d[len(i)]=[i]
print(d)
