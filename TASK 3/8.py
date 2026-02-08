n=list(map(int,input().split()))
max_right=-1
found=False
for i in range(len(n)-1,-1,-1):
    if n[i]>=max_right:
        print(n[i])
        max_right=n[i]
        found=True
if found==False:
    print("No")
        
