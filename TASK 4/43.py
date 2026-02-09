dt = [
    (1, 101),
    (1, 102),
    (2, 101),
    (2, 103),
    (3, 104),
    (3, 101)
]

sc = {}
ac = {}

for s, a in dt:
    sc[s] = sc.get(s, 0) + 1
    ac[a] = ac.get(a, 0) + 1

print(sc)

for a in ac:
    if ac[a] > 1:
        print(a)
