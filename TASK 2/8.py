n=int(input("Enter no of runners:"))
mt=float('inf')
for i in range(n):
    t=float(input("Enter time:"))
    if t<mt:
        mt=t
print(mt)
    
