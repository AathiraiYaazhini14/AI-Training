p= {
    "Alice": 4500,
    "Bob": 6000,
    "Charlie": 12000
}
d={}
for i in p:
    if p[i]>5000:
        d[i]=(p[i]*10/100)
    elif p[i]>10000:
        d[i]=(p[i]*20/100)
    else:
        d[i]=p[i]
print(d)
