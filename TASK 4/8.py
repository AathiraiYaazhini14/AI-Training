temps = [
    [30, 32, 31, 29, 28, 30, 31],
    [33, 34, 32, 31, 30, 29, 28],
    [27, 28, 29, 30, 31, 32, 33]
]
m=0
ma=0
for i in temps:
    a=(sum(i)/len(i))
    print(a)
    if m<max(i):
        m=max(i)
    if ma<a:
        ma=a
print(m,ma)
