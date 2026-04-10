class User:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, v):
        if 0 <= v <= 150:
            self._age = v
        else:
            raise ValueError("Invalid age!")


user_1 = User(25)
user_1.age = -5 #Shouldn't work