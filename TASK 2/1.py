st=input("Enter number:")
length=len(st)
half=int(len(st)/2)
s1=st[0:half]
s2=st[half:length]
ns1=int(s1)
ns2=int(s2)
sns1,sns2=0,0
while ns1!=0:
    dig=ns1%10
    sns1+=dig
    ns1//=10
while ns2!=0:
    dig=ns2%10
    sns2+=dig
    ns2//=10
if sns1==sns2:
    print("Balanced")
else:
    print("Not balanced")
