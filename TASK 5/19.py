from abc import ABC, abstractmethod

class MLModel(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def predict(self):
        pass


class LinearModel(MLModel):
    def predict(self):
        return sum(self.data) / len(self.data)


class TreeModel(MLModel):
    def predict(self):
        return max(self.data)


if __name__ == "__main__":
    models = [
        LinearModel([1, 2, 3, 4]),
        TreeModel([1, 2, 3, 4])
    ]

    for model in models:
        print("Prediction:", model.predict())
