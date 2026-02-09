dt = [
    ("B1", 100),
    ("B2", 150),
    ("B1", 200),
    ("B3", 180),
    ("B2", 120)
]

hb = {}
mx = -1
mb = ""

for b, a in dt:
    if b not in hb or a > hb[b]:
        hb[b] = a
    if a > mx:
        mx = a
        mb = b

print(hb)
print(mb)
