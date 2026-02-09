skills = {
    "Alice": {"Python", "SQL", "Java"},
    "Bob": {"Python", "SQL"},
    "Charlie": {"Python", "C++"}
}
s=set()
for i in skills:
    if "Python" in skills[i] and 'SQL' in skills[i]:
        print(i)
    s=s|skills[i]
print(s)
val=list(skills.values())
cs=val[0]
for i in val[1:]:
    cs=cs&i
print(cs)
