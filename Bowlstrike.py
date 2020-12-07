class BowlingGame(object):
    def __init__(self):
        self.throws = []
        self.score = 0

    def throw(self,pins):
        self.throws.append(pins)

    def calculate_score(self):
        ball = 0
        for frames in range(10):
            #print("Frame ", frames)
            #print(ball)
            if self.throws[ball] == 10:
                self.score +=10 + self.throws[ball + 1] + self.throws[ball +2]
                ball += 1
            elif self.throws[ball] + self.throws[ball + 1] == 10:
                self.score += 10 + self.throws [ball + 2]
                ball += 2
            else:
                self.score += self.throws[ball] + self.throws[ball + 1]
                ball += 2
 