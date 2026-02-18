class Emp:
    def __init__(self, sal):
        self.__sal = sal

    def get_salary(self):
        return self.__sal

    def update_salary(self, amt):
        if amt <= 0:
            print("Invalid increment amount.")
            return
        self.__sal += amt
        print("Salary updated successfully.")
        print("Your salary now is", self.__sal)


es = Emp(5000)
print("Current Salary:", es.get_salary())
es.update_salary(1000)
print("Updated Salary:", es.get_salary())
