p= ["abc123!", "password", "pass@1", "hello#", "12345"]
vp=[]
ip=[]
for i in p:
    if any(c.isdigit()for c in p)and any(not c.isalnum()for c in p):
        vp.append(i)
    else:
        ip.append(i)
print(vp)
print(ip)
