readings = [
    {"id": 1, "temp": 30, "humidity": 60},
    {"id": 2, "temp": 31, "humidity": 58, "pressure": 1012},
    {"id": 3, "temp": 29, "humidity": 61}
]

key_count = {}

for r in readings:
    k = tuple(sorted(r.keys()))
    key_count[k] = key_count.get(k, 0) + 1

correct_keys = max(key_count, key=key_count.get)

for r in readings:
    if tuple(sorted(r.keys())) != correct_keys:
        print(r)
