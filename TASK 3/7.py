nn=[[1,2],[3,4],[5]]
flat=[]
for i in nn:
    if isinstance(i,list):
        flat.extend(i)
    else:
        flat.append(i)
print(flat)
