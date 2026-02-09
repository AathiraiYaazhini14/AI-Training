slots = [
    ("Alice", 1),
    ("Bob", 2),
    ("Charlie", 1)
]
l=[]
k=[]
for i in slots:
    l.append(i[0])
    k.append(i[1])
if len(set(l))!=len(l):
    print("Names are repeated")
if len(set(k))!=len(k):
    print("Slots are repeated")
