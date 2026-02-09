data = {
    "A": {"B", "C"},
    "B": {"A"},
    "C": {"A"},
    "D": set(),
    "E": {"F"},
    "F": {"E"},
    "G": {"A"}
}

mutual = []
chosen = set()

for s in data:
    for p in data[s]:
        if p in data and s in data[p]:
            pair = tuple(sorted((s, p)))
            if pair not in mutual:
                mutual.append(pair)
        chosen.add(p)

isolated = []
for s in data:
    if s not in chosen:
        isolated.append(s)

print(mutual)
print(isolated)
