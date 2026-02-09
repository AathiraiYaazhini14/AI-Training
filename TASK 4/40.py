dt = [
    {"id": 1, "tg": ["ai", "ml", "nlp"]},
    {"id": 2, "tg": ["ai", "ml"]},
    {"id": 3, "tg": ["ai", "ml", "cv"]}
]

ok = 1
cm = set(dt[0]["tg"])

for d in dt:
    if len(d["tg"]) == 0:
        ok = 0
    cm = cm.intersection(d["tg"])

if ok:
    print("all tagged")
else:
    print("empty tag found")

print(cm)
