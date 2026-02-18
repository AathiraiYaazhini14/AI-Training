from datetime import datetime

class Experiment:
    def __init__(self, exp_id):
        self.exp_id = exp_id
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = datetime.now()
        print(f"{self.exp_id} started at {self.start_time}")

    def end(self):
        if not self.start_time:
            print(f"{self.exp_id} has not been started yet.")
            return
        self.end_time = datetime.now()
        duration = self.end_time - self.start_time
        print(f"{self.exp_id} ended at {self.end_time}")
        print(f"Duration: {duration}")


exp1 = Experiment("EXP001")
exp1.start()
exp1.end()

exp2 = Experiment("EXP002")
exp2.end()
exp2.start()
