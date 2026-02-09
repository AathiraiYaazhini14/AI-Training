c = {
    "Math": {101, 102, 103, 104},
    "Physics": {102, 105, 106},
    "Chemistry": {101, 103, 107},
    "Biology": {108, 109}
}

sc = {}

for x, y in c.items():
    for z in y:
        if z in sc:
            sc[z].append(x)
        else:
            sc[z] = [x]

m = []
for a, b in sc.items():
    if len(b) > 1:
        m.append(a)

mx = 0
for y in c.values():
    if len(y) > mx:
        mx = len(y)

mc = []
for x, y in c.items():
    if len(y) == mx:
        mc.append(x)

print(m)
print(mc)
