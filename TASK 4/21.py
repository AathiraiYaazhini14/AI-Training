q = {
    "Alice": [1, 2, 3, 4],
    "Bob": [2, 3, 4, 5],
    "Charlie": [1, 2, 3, 4, 5]
}

a = set()
for v in q.values():
    a.update(v)
print(a)
print(len(a))

r = []
for s, v in q.items():
    o = set()
    for t, w in q.items():
        if t != s:
            o.update(w)
    if set(v) >= o:
        r.append(s)
print(r)
