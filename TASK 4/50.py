dt = {
    "P1": ["AI", "ML", "NLP"],
    "P2": ["AI", "ML", "CV"],
    "P3": ["AI", "ML", "DL", "CV"]
}

all_kw = set()
cm_kw = set(dt[list(dt.keys())[0]])
mx = 0
mp = ""

for p in dt:
    s = set(dt[p])
    all_kw.update(s)
    cm_kw = cm_kw.intersection(s)
    if len(s) > mx:
        mx = len(s)
        mp = p

print(all_kw)
print(cm_kw)
print(mp)
