fi={"age":2.5,"salary":1.5,"experience":1.0,"education":0.5}

ts=sum(fi.values())
nf={k:v/ts for k,v in fi.items()}

print(nf)
