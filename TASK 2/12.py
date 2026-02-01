n=int(input("Enter amnt:"))
notes=[500, 200, 100, 50, 20, 10, 1]
total=0
for i in notes:
    total+=n//i
    n%=i
print(total)
