
from src.util import get_winner


class Bracket(object):

    def __init__(self, data):
        self.input = data
        self.run_history = []
        self.run_function = get_winner

    def run(self, display_winner=True, display_history=False):
        winner = get_winner(
            self.input,
            self.run_history
        )
        if display_winner:
            print("%s wins the tournament!" % winner["team"])
        if display_history:
            for history_item in self.run_history:
                print("%s" % history_item)
        




