# Learning @property
class Employee:
    def __init__(self, _name):
        self._name = _name

    @property
    def name(self):
        return self._name

e1 = Employee("Oli")
print(e1.name)