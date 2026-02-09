dt = {
    "A": [120, 130, 125],
    "B": [90, 100, 95],
    "C": [150, 160, 155]
}

av = {}
mx = -1
mc = ""

for c in dt:
    s = 0
    for v in dt[c]:
        s += v
    a = s / len(dt[c])
    av[c] = a
    if a > mx:
        mx = a
        mc = c

print(av)
print(mc)
