s=input()
s=s.lower()
sc=set(s)
c=0
for i in sc:
    if i!=" ":
        c+=1
print(c)
