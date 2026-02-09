visits = [
    {"patient_id": 1, "doctor": "DrA", "visit_count": 3},
    {"patient_id": 2, "doctor": "DrB", "visit_count": 2},
    {"patient_id": 3, "doctor": "DrA", "visit_count": 1},
    {"patient_id": 4, "doctor": "DrC", "visit_count": 4}
]

d = {}

for v in visits:
    doc = v["doctor"]
    d[doc] = d.get(doc, 0) + v["visit_count"]

print(d)
