records = [
    {"id": 1, "name": "Alice", "dept": "CSE"},
    {"id": 2, "name": "Bob", "dept": "ECE"},
    {"id": 3, "name": "Charlie", "dept": "ME"},
    {"id": 1, "name": "Alice", "dept": "CSE"},
    {"id": 4, "name": "David", "dept": "CSE"},
    {"id": 2, "name": "Bob", "dept": "ECE"}
]

tuples = [tuple(sorted(r.items())) for r in records]

duplicates = []
for t in set(tuples):
    if tuples.count(t) > 1:
        duplicates.append(dict(t))

print(duplicates)
