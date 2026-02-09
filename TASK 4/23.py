logs = [(101, "09:00"), (102, "09:05"), (101, "09:00"), (103, "09:10"), (102, "09:05")]

v = set()
i = []

for e, t in logs:
    if (e, t) in v:
        i.append((e, t))
    else:
        v.add((e, t))

print(i)
