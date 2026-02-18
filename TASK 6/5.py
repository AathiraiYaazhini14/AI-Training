from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def predict(self, data):
        pass

class LinearModel(Model):
    def predict(self, data):
        return [x*2 for x in data]

class TreeModel(Model):
    def predict(self, data):
        return [x+5 for x in data]

def run_predictions(model, data):
    print(model.predict(data))

data = [1,2,3]
run_predictions(LinearModel(), data)
run_predictions(TreeModel(), data)
