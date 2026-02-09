dt = {
    "E1": {"A", "B", "C"},
    "E2": {"A", "B"},
    "E3": {"A", "C"},
    "E4": {"D"}
}

cm = set(dt[list(dt.keys())[0]])
for e in dt:
    cm = cm.intersection(dt[e])

print(cm)

all_cert = {}
for e in dt:
    for c in dt[e]:
        all_cert[c] = all_cert.get(c, 0) + 1

for e in dt:
    for c in dt[e]:
        if all_cert[c] == 1:
            print(e)
            break
