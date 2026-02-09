res= [
    ("A", 1),
    ("A", 2),
    ("B", 1),
    ("B", 2)
]
s=[]
for i in res:
    s.append(i[0])

if len(set(s))!=len(s):
    print("Dup seats")
print(len(set(s)))
