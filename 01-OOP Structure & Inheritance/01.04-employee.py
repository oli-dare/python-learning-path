class Employee:
    def __init__(self, _salary):
        self._salary = _salary

    @property
    def salary(self):
        return f"Confidential: {self._salary} Euro."

employee = Employee(5000)
print(employee.salary)