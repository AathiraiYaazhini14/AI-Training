days=int(input("Enter days:"))
years=days//365
weeks=(days-(years*365))//7
day=days-(years*365)-(weeks*7)
print(years,"years",weeks,"weeks",day,"days")
