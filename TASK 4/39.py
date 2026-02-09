dt = [
    ("Al", 150),
    ("Bo", 200),
    ("Ch", 180),
    ("Da", 120)
]

pl = set()
ok = 1

for p, s in dt:
    if p in pl:
        ok = 0
        break
    pl.add(p)

if ok:
    print("valid")
else:
    print("dup")

sb = sorted(dt, key=lambda x: x[1], reverse=True)
print(sb)
