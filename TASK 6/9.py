import math


class DataReader:
    def __init__(self):
        self._data = []

    def add(self, value: float):
        self._data.append(value)

    def get_data(self):
        return self._data


class Statistics:
    def __init__(self, data):
        self._data = data

    def average(self):
        if not self._data:
            return 0
        return sum(self._data) / len(self._data)

    def spread(self):
        if not self._data:
            return 0
        return max(self._data) - min(self._data)

    def standard_deviation(self):
        if not self._data:
            return 0
        mean = self.average()
        variance = sum((x - mean) ** 2 for x in self._data) / len(self._data)
        return math.sqrt(variance)


reader = DataReader()

numbers = [12, 18, 25, 30, 45]

for num in numbers:
    reader.add(num)

stats = Statistics(reader.get_data())

print("Average:", stats.average())
print("Spread:", stats.spread())
print("Standard Deviation:", stats.standard_deviation())
