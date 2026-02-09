p = [12, 15, 8, 20, 18]

m = max(p)
s = p.index(m) + 1
print(s, m)

a = sum(p) / len(p)
b = [i+1 for i, v in enumerate(p) if v < a]
print(b)
