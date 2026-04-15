class LeaderBoard:
    def __init__(self, score):
        self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score_value):
        if 0 <= score_value <= 1000000:
            self._score = score_value
        else:
            raise ValueError("Invalid Score!")


p1 = LeaderBoard(500)
# p1.score = 1500000 would not work
p1.score = 400
p1.score = 600
print(p1.score)


