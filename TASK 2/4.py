a=int(input("Enter age:"))
ticket=0
if a<=5:
    pass
elif a>5 and a<=12:
    ticket=200-(200*50/100)
elif a>13 and a<=59:
    ticket=200
else:
    ticket=200-(200*30/100)
print(ticket)
