n = input("Enter number:")

digits = set(n)

for i in range(10):
    if str(i) not in digits:
        print(i)
        break
