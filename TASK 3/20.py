s=input()
dic={'a':0,'d':0,'sp':0}
a,d,sp=0,0,0
for i in s:
    if i.isalpha():
        dic['a']+=1
    elif i.isdigit():
        dic['d']+=1
    else:
        dic['sp']+=1
print(dic)
