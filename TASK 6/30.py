class Evaluation:
    def calculate(self, marks):
        pass

class Percentage(Evaluation):
    def calculate(self, marks):
        return sum(marks)/len(marks)

class Grade(Evaluation):
    def calculate(self, marks):
        return "Pass" if sum(marks)/len(marks) > 50 else "Fail"

def engine(e, marks):
    print(e.calculate(marks))

engine(Percentage(), [80,90])
engine(Grade(), [40,50])
