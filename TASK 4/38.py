avg_delay = {}
max_avg = 0
max_flight = None

for flight in data:
    delays = data[flight]
    if len(delays) > 0:
        avg = sum(delays) / len(delays)
    else:
        avg = 0

    avg_delay[flight] = avg

    if avg > max_avg:
        max_avg = avg
        max_flight = flight

print(avg_delay)
print(max_flight)
