dt = {
    "D1": [2, 3, 1],
    "D2": [4, 2, 3],
    "D3": [1, 1, 2]
}

tot = {}
s = 0

for d in dt:
    t = sum(dt[d])
    tot[d] = t
    s += t

avg = s / len(dt)

print(tot)

for d in tot:
    if tot[d] > avg:
        print(d)
