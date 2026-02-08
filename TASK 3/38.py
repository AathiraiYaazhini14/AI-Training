d={"aa":'aids','bb':'aiml','cc':'cse'}
nd={}
for s,k in d.items():
    nd.setdefault(k,[]).append(s)
print(nd)
