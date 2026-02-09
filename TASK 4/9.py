scores = {
    "Alice": [80, 90, 85],
    "Bob": [60, 70, 65],
    "Charlie": [90, 95, 92]
}
ca=0
l={}
for i in scores:
    a=sum(scores[i])/len(scores[i])
    ca+=a
    l[i]=a
    print(a)
cls=ca/len(scores)
for i in l:
    if l[i]>cls:
        print(i)
