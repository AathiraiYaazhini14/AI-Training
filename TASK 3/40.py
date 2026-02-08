ld=[
{"id":1,"name":"A"},
{"id":2,"nam":"B"}
]
f=True
kc=ld[0].keys()
for i in ld:
    k=i.keys()
    if kc!=k:
        f=False
        break
if f:
    print("Same")
else:
    print("Not same")
