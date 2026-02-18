import statistics

class Metrics:
    def __init__(self, scores):
        self.scores = scores

    def compute(self):
        print(statistics.mean(self.scores))
        print(statistics.pvariance(self.scores))

Metrics([80,90,85]).compute()
