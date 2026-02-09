doc1 = ["machine", "learning", "is", "fun"]
doc2 = ["machine", "is", "deep", "fun"]
a=set(doc1)&set(doc2)
b=set(doc1)|set(doc2)
k=(len(a)/len(b))
print(k)
if k>=0.5:
    print("Similar")
else:
    print("Not similar")
