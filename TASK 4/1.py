s= {
    "Alice": ["Python Basics", "Loops", "Functions"],
    "Bob": ["Python Basics", "Loops"],
    "Charlie": ["Python Basics", "Loops", "Functions", "OOP"]
}
m=0
for i in s:
    print(len(s[i]))
    if m<len(s[i]):
        m=len(s[i])
print(m)
