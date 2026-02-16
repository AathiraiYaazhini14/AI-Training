from abc import ABC, abstractmethod

class InferenceEngine(ABC):
    @abstractmethod
    def infer(self, data):
        pass


class RuleBasedEngine(InferenceEngine):
    def infer(self, data):
        return "Rule-based result"


class MLBasedEngine(InferenceEngine):
    def infer(self, data):
        return "ML-based prediction"


if __name__ == "__main__":
    engines = [RuleBasedEngine(), MLBasedEngine()]
    for engine in engines:
        print(engine.infer("sample data"))
