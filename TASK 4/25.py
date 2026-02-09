sales = {
    "Electronics": [1200, 1500, 800],
    "Clothing": [500, 700, 300],
    "Books": [200, 150, 400]
}

t = {}
for c, v in sales.items():
    t[c] = sum(v)

h = max(t, key=t.get)

print(t)
print(h)
