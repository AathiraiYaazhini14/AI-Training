m=[[1,2,3],[4,5,6],[7,8,9]]
ps,ss=0,0
for i in range(3):
    for j in range(3):
        if i==j:
            ps+=m[i][j]
        if i+j==3-1:
            ss+=m[i][j]
print(ps,ss)
        
