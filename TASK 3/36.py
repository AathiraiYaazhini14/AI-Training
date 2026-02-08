s={'a':2, 'b':3, 'c':5}
c={'b':1, 'a':4}
for i in s:
    if i in c:
        s[i]+=c[i]
print(s)
