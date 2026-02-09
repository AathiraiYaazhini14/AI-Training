dt = [
    {"id": 1, "rs": "R1", "it": ["Burger", "Fries"]},
    {"id": 2, "rs": "R2", "it": ["Pizza"]},
    {"id": 3, "rs": "R1", "it": ["Burger", "Burger"]},
    {"id": 4, "rs": "R3", "it": []}
]

ok = 1
dup_rs = set()

for d in dt:
    if len(d["it"]) == 0:
        ok = 0
    if len(d["it"]) != len(set(d["it"])):
        dup_rs.add(d["rs"])

if ok:
    print("all orders valid")
else:
    print("empty orders found")

print(dup_rs)
