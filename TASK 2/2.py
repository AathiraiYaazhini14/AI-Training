amt=int(input("Enter withdrawal amount:"))
bal=int(input("Enter balance:"))
if amt%100==0 and amt<=bal:
    if (bal-amt)>500:
        print("Valid")
    else:
        print("Not Valid")
else:
    print("Not valid")
        
