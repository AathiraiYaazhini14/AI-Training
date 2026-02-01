n=int(input("Enter amnt:"))
bill=0
if n<1000:
    print("No discount")
elif n>=1000 and n<=2999:
    bill=n-(n*10/100)
elif n>=3000 and n<=4999:
    bill=n-(n*20/100)
else:
    bill=n-(n*30/100)
print(bill)
