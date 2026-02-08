s = [
    {"name": "Alice", "marks": 85, "attendance": 90},
    {"name": "Bob", "marks": 78, "attendance": 95},
    {"name": "Charlie", "marks": 92, "attendance": 85},
    {"name": "David", "marks": 88, "attendance": 80}
]
d={}
for i in s:
    index=(i['marks']*0.7)+(i['attendance']*0.3)
    d[i['name']]=index
print(d)
topper=max(d,key=d.get)
print(topper)
