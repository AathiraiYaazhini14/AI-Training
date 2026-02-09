posts = [
    ["#fun", "#travel", "#sunset"],
    ["#travel", "#food", "#fun"],
    ["#fun", "#travel", "#photography"]
]
uni=set()
for p in posts:
    for tag in p:
        uni.add(tag)
com=set(posts[0])
for p in posts[1:]:
    com=com.intersection(p)
print(uni)
print(com)
