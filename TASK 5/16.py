from abc import ABC, abstractmethod

class GradingPolicy(ABC):
    @abstractmethod
    def compute_grade(self, marks):
        pass


class PercentagePolicy(GradingPolicy):
    def compute_grade(self, marks):
        return "A" if marks >= 75 else "B"


class GPAPolicy(GradingPolicy):
    def compute_grade(self, marks):
        return round(marks / 10, 2)


if __name__ == "__main__":
    policies = [PercentagePolicy(), GPAPolicy()]
    for policy in policies:
        print(policy.compute_grade(82))
