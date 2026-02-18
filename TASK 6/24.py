class Workout:
    def calories(self):
        pass

class Running(Workout):
    def calories(self):
        return 300

class Swimming(Workout):
    def calories(self):
        return 400

def track(w):
    print(w.calories())

track(Running())
track(Swimming())
