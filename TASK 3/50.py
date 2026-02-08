ds=[
    {"name":"Alice","dept":"CSE","gender":"F"},
    {"name":"Bob","dept":"CSE","gender":"M"},
    {"name":"Charlie","dept":"ECE","gender":"M"},
    {"name":"David","dept":"ME","gender":"M"},
    {"name":"Eve","dept":"ECE","gender":"F"},
    {"name":"Frank","dept":"ME","gender":"M"}
]

rw=len(ds)
uv={}

for d in ds:
    for k,v in d.items():
        uv.setdefault(k,set()).add(v)

for k in uv:
    uv[k]=len(uv[k])

sm={"rows":rw,"unique_values":uv}
print(sm)
