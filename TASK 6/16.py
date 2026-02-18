import random
from datetime import datetime

class Trainer:
    def __init__(self, data):
        self.data = data

    def train(self):
        random.shuffle(self.data)
        print(datetime.now())
        print(self.data)

Trainer([1,2,3,4]).train()
