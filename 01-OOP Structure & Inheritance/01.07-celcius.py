class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError
        self._temperature = value


human_body = Celsius(37)
print(human_body.temperature)

human_body.temperature = -300 # Should raise ValueError