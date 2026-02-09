cart_day1 = {"apple": 2, "banana": 3, "milk": 1}
cart_day2 = {"banana": 2, "milk": 2, "bread": 1}
for i in cart_day1:
    if i in cart_day2:
        cart_day2[i]+=cart_day1[i]
    else:
        cart_day2[i]=cart_day1[i]
print(cart_day2)
