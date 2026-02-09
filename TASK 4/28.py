reports = [
    {"app": "1.0", "device": "Android", "severity": "HIGH"},
    {"app": "1.0", "device": "iOS", "severity": "LOW"},
    {"app": "1.1", "device": "Android", "severity": "HIGH"},
    {"app": "1.0", "device": "Android", "severity": "MEDIUM"}
]
d={}
for i in reports:
    if i['severity']=='HIGH':
        print(i)
    d[i['app']]=d.get(i['app'],0)+1
print(d)
