import unittest
from Bowlstrike import BowlingGame

class BowlingGameTests(unittest.TestCase):
    def throw_many(self, game, number_of_times, pins):
        for _ in range(number_of_times):
            game.throw(pins)

    def test_all_gutters(self):
        #print("test_all_gutters")
        game = BowlingGame()
        self.throw_many(game, 20, 0)
        game.calculate_score()
        self.assertEqual(game.score, 0)

    def test_perfect_game(self):
        #print("test_perfect_game")
        game = BowlingGame()
        self.throw_many(game, 12, 10)
        game.calculate_score()
        self.assertEqual(game.score, 300)

    def test_all_ones(self):
        #print("test_all_ones")
        game = BowlingGame()
        number_of_times = 20
        pins = 1
        self.throw_many(game, number_of_times, pins)
        game.calculate_score()
        self.assertEqual(game.score, 20)

    def test_different_throws(self):
        #print("test_different_throws")
        game = BowlingGame()
        game.throw(6)
        game.throw(0)
        game.throw(7)
        game.throw(0)
        game.throw(2)
        for _ in range(15):
            game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 15)

    def test_for_spare(self):
        #print("test_for_spare")
        game = BowlingGame()
        game.throw(4)
        game.throw(6)
        game.throw(7)
        game.throw(0)
        for _ in range(16):
            game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 24)

    def test_for_strike(self):
        #print("test_for_strike")
        game = BowlingGame()
        game.throw(10)
        game.throw(4)
        game.throw(2)
        self.throw_many(game, 17,0)
        game.calculate_score()
        self.assertEqual(game.score, 22)

if __name__ == '__main__':
    unittest.main()