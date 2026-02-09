dt = {
    "A": {1, 2, 3, 4},
    "B": {1, 2},
    "C": {1, 2, 3, 4},
    "D": {1},
    "E": set()
}

al = set()
for s in dt:
    al.update(dt[s])

n = len(al)

for s in dt:
    if dt[s] == al:
        print(s)

for s in dt:
    if len(dt[s]) < n/2:
        print(s)
