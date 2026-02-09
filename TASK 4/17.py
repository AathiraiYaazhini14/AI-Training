students = [
    {"name": "Alice", "dept": "CSE", "cgpa": 8.5},
    {"name": "Bob", "dept": "ECE", "cgpa": 7.8},
    {"name": "Charlie", "dept": "CSE", "cgpa": 9.0},
    {"name": "David", "dept": "ME", "cgpa": 8.0}
]

total = {}
count = {}

for i in students:
    dept = i['dept']
    cgpa = i['cgpa']

    total[dept] = total.get(dept, 0) + cgpa
    count[dept] = count.get(dept, 0) + 1

avg = {}
for d in total:
    avg[d] = total[d] / count[d]

print(avg)
