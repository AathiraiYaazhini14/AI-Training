votes = [
    ("V1", "Alice"),
    ("V1", "Alice"),
    ("V2", "Bob"),
    ("V2", "Bob")
]
f={}
for i in votes:
    f[i]=f.get(i,0)+1
for i in f:
    if f[i]>1:
        print(i)
        f[i]=1
print(f)
    
