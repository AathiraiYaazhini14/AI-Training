req = {"Python", "ML", "AI", "SQL", "Data"}

res = {
    "R1": ["Python", "ML", "AI", "SQL"],
    "R2": ["Python", "SQL"],
    "R3": ["Python", "ML", "AI", "SQL", "Data"]
}

for r in res:
    s = set(res[r])
    match = len(s.intersection(req)) / len(req)
    if match >= 0.7:
        print(r)
    print(r, req - s)
