import unittest
from src.bracket import Bracket
from src.util import winner_heuristic, get_winner

class TestBracketMethod(unittest.TestCase):

    def setUp(self):
        self.team_one_name = "Zack"
        self.team_one_seed = 1
        self.team_one = {
            "team" : self.team_one_name,
            "seed" : self.team_one_seed
        }
        self.team_two_name = "Mira"
        self.team_two_seed = 2
        self.team_two = {
            "team" : self.team_two_name,
            "seed" : self.team_two_seed
        }
        self.team_three_name = "Niko"
        self.team_three_seed = 3
        self.team_three = {
            "team" : self.team_three_name,
            "seed" : self.team_three_seed
        }
        self.team_four_name = "The Bulls"
        self.team_four_seed = 4
        self.team_four = {
            "team" : self.team_four_name,
            "seed" : self.team_four_seed
        }

    def test_winner_heuristic(self):
        winner = winner_heuristic(
            self.team_one, self.team_two, []
        )
        self.assertEqual(winner["team"], self.team_one_name)

    def test_get_winner(self):

        _input = {
            "1" : {
                "1" : self.team_one,
                "2" :  self.team_four
            },
            "2" : {
                "1" : self.team_two,
                "2" : self.team_three
            }
        }

        run_history = []
        winner = get_winner(_input, run_history)
        self.assertEqual(
            winner["team"], self.team_one_name
        )


if __name__ == '__main__':
    unittest.main()
