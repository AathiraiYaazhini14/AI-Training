data = [
    {"account_id": 101, "amount": 500, "type": "CREDIT"},
    {"account_id": 102, "amount": 300, "type": "CREDIT"},
    {"account_id": 101, "amount": 200, "type": "DEBIT"},
    {"account_id": 103, "amount": 1000, "type": "CREDIT"},
    {"account_id": 102, "amount": 100, "type": "DEBIT"},
    {"account_id": 101, "amount": 300, "type": "CREDIT"}
]

bal = {}

for i in data:
    acc = i["account_id"]
    amt = i["amount"]
    if acc not in bal:
        bal[acc] = 0
    if i["type"] == "CREDIT":
        bal[acc] += amt
    else:
        bal[acc] -= amt

print(bal)

mx = max(bal, key=bal.get)
print(mx)
