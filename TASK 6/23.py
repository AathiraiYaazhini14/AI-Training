class Report:
    def generate(self):
        pass

class SalesReport(Report):
    def generate(self):
        print("Sales Report")

class FinanceReport(Report):
    def generate(self):
        print("Finance Report")

def run(report):
    report.generate()

run(SalesReport())
run(FinanceReport())
