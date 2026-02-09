records = [
    {"student": "Alice", "book": "Python", "days": 5},
    {"student": "Bob", "book": "Java", "days": 10},
    {"student": "Alice", "book": "Python", "days": 12},
    {"student": "Charlie", "book": "C++", "days": 7}
]
l={}
for i in records:
    if i['days']>7:
        print(i['student'])
    
    l[i['book']]=l.get(i['book'],0)+1
print(l)
    
