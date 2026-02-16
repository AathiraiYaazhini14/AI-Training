from abc import ABC, abstractmethod

class Exam(ABC):
    def __init__(self, subject, max_marks):
        self.subject = subject
        self.max_marks = max_marks

    @abstractmethod
    def evaluate(self, marks):
        pass


class TheoryExam(Exam):
    def evaluate(self, marks):
        return min(marks, self.max_marks)


class PracticalExam(Exam):
    def evaluate(self, marks):
        return min(marks + 5, self.max_marks)


if __name__ == "__main__":
    exams = [
        TheoryExam("Math", 100),
        PracticalExam("Physics Lab", 50)
    ]

    for exam in exams:
        print(exam.subject, "Marks:", exam.evaluate(45))
