unit=int(input("Enter units:"))
if unit<100:
    bill=units*2
elif unit>100 and unit<=200:
    bill=100*2+(unit-100)*3
elif unit>200 and unit<=300:
    bill=100*2+100*3+(unit-200)*4
else:
    bill=100*2+100*3+100*4+(unit-300)*5
print(bill)
