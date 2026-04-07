class ModelConfig:
    def __init__(self, _lr):
        self._lr = _lr

    @property
    def lr(self):
        return self._lr

    @lr.setter
    def lr(self, value):
        if value <= 0:
            raise ValueError("Learning rate must be positive!")
        self._lr = value


config = ModelConfig(0.01)
config.lr = 0.05
print(config.lr)
config.lr = -1
print(config.lr)