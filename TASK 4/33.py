data = {
    "Morning": {1, 2, 3, 4, 5},
    "Afternoon": {2, 3, 4, 5},
    "Evening": {1, 2, 3, 4, 5},
    "Night": {2, 3, 4, 5}
}
day=set()
for i in data:
    day.update(data[i])
for i in data:
    if data[i]==day:
        print(i)
com=day.copy()
for c in data.values():
    com=com.intersection(c)
print(com)
