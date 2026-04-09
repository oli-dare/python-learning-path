class Engine:
    def __init__(self, _speed):
        self.speed = _speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, v):
        if v > 200:
            print("Speed limit reached!")
            self._speed = 200
        else:
            self._speed = v


engine_1 = Engine(50)
engine_1.speed = 250 # Testing if this works
print(engine_1.speed) #250 (it worked)
