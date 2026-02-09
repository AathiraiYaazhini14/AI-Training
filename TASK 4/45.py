dt = [
    {"id": 1, "ct": "A", "st": 10},
    {"id": 2, "ct": "B", "st": 0},
    {"id": 3, "ct": "A", "st": 5},
    {"id": 4, "ct": "C", "st": 0}
]

ok = 1
oc = set()

for d in dt:
    if d["st"] <= 0:
        ok = 0
        oc.add(d["ct"])

if ok:
    print("all in stock")
else:
    print("out of stock found")

print(oc)
