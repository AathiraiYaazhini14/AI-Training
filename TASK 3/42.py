students = [
    {"name": "Alice", "dept": "CSE", "marks": 85},
    {"name": "Bob", "dept": "CSE", "marks": 92},
    {"name": "Charlie", "dept": "ECE", "marks": 88},
    {"name": "David", "dept": "ECE", "marks": 91},
    {"name": "Eve", "dept": "ME", "marks": 78},
    {"name": "Frank", "dept": "ME", "marks": 82}
]
dm={}
for i in students:
    dm.setdefault(i['dept'],[]).append(i['marks'])
print(dm)
for i in dm:
    print(max(dm[i]))
