dt = {
    "U1": [1.2, 1.5, 2.0],
    "U2": [0.5, 0.7, 0.6],
    "U3": [2.5, 2.0, 3.0]
}

lm = 4.0

mx = -1
mu = ""

for u in dt:
    s = 0
    for v in dt[u]:
        s += v

    if s > lm:
        print(u)

    a = s / len(dt[u])
    if a > mx:
        mx = a
        mu = u

print(mu)
