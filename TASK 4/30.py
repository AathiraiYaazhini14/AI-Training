data = {
    "A": [1, 2, 3,5],        
    "B": [1, 2],           
    "C": [1, 2, 3],        
    "D": [2, 3],           
    "E": [],            
    "F": [1],           
}
a=set()
for i in data:
    a.update(data[i])
for i in data:
    if set(data[i])==a:
        print(i)
for i in range(1,max(a)+1):
    if i not in a:
        print(i)
