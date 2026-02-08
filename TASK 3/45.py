rs= {
    "python": 0.4,
    "machine learning": 0.3,
    "sql": 0.2,
    "communication": 0.1
}

cs = {
    "python": 8,
    "machine learning": 7,
    "sql": 6,
    "java": 5
}
score=0
for i in cs:
    if i in rs:
        score+=(rs[i]*cs[i])
print(f'{score:.2f}')

