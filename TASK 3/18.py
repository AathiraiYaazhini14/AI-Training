mrk={'aa':[10,20,30],'bb':[30,40,10],'cc':[90,40,50]}
avgm={}
for k,v in mrk.items():
    avg=sum(v)/len(v)
    avgm[k]=avg
print(avgm)
