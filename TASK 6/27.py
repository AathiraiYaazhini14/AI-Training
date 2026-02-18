from datetime import datetime

class Experiment:
    def run(self):
        start = datetime.now()
        print("Start:", start)
        end = datetime.now()
        print("End:", end)

Experiment().run()
