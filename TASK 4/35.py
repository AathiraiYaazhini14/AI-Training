data = {
    "D1": ["ON", "ON", "OFF", "ON"],
    "D2": ["ON", "ON", "ON"],
    "D3": ["OFF", "OFF"],
    "D4": ["ON", "OFF"],
    "D5": ["ON"]
}
won=[]
woff=[]
for i in data:
    if 'OFF' in data[i]:
        woff.append(i)
    else:
        won.append(i)
print("Went on:",won)
print("Went off:",woff)
