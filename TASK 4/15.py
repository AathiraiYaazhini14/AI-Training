a= {
    "Ravi": {"Mon", "Tue"},
    "Anu": {"Mon", "Tue", "Wed"},
    "Kiran": {"Mon", "Tue", "Wed", "Thu",'Fri','Sat'}
}
d={}
for i in a:
    d[i]=len(a[i])
print(d)
for i in d:
    if d[i]==6:
        print(i)
