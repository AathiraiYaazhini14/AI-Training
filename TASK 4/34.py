re = [
    {"r": 1, "sentiment": "Positive"},
    {"r": 2, "sentiment": "Negative"},
    {"r": 3, "sentiment": "Positive"},
    {"r": 4, "sentiment": "Neutral"},
    {"r": 5, "sentiment": "Positive"},
    {"r": 6, "sentiment": "Negative"}
]
d={}
for i in re:
    d[i['sentiment']]=d.get(i['sentiment'],0)+1
print(d)
mx=max(d,key=d.get)
print(mx)
