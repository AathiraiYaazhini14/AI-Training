scores = [
    ("Alice", 100),
    ("Bob", 90),
    ("Charlie", 90),
    ("David", 80),
    ("Eve", 70)
]

ss=sorted(scores,key=lambda x:x[1],reverse=True)
ranked=[]
rank=1
prev=None
for i,(name,score) in enumerate(score):
    if score!=prev:
        rank=i+1
    ranked.append((name,score,rank))
    prev=score
