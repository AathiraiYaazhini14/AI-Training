files = ["report.pdf", "data.csv", "image.png", "notes.txt", "summary.pdf"]
d={}
for i in files:
    name,ext=i.rsplit('.',1)
    if ext not in d:
        d[ext]=[i]
    else:
        d[ext].append(i)
print(d)
