ev= {
    "ai", "machine", "learning", "data", "model", "training"
}

doc= [
    "ai and data drive modern systems",
    "machine learning models improve with training data",
    "deep learning is powerful"
]
f=set()
for d in doc:
    for word in d.lower().split():
        f.add(word)
covered=ev&f
missing=ev-f
print((len(covered)/len(ev))*100,missing)
