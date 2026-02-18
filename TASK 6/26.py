import random

class Sampler:
    def __init__(self, data):
        self.data = data

    def sample(self, n):
        return random.sample(self.data, n)

print(Sampler([1,2,3,4,5]).sample(2))
