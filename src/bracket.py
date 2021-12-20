
def validate_side(side):
    not_base_case = ('team' not in side and 'seed' not in side)
    not_recursive_case = ('1' not in side and '2' not in side)
    if not_base_case and not_recursive_case:
        raise Exception("%s" % side)

def winner_heuristic(team_one, team_two, run_history):
    if team_one['seed'] > team_two['seed']:
        run_history.append(
            '%s defeats %s' % (
                team_one['team'], team_two['team']
            )
        )
        return team_one
    else:
        run_history.append(
            '%s defeats %s' % (
                team_two['team'], team_one['team']
            )
        )
        return team_two

def get_winner(side, run_history):
    validate_side(side)
    if 'team' in side['1']:
        if 'team' in side['2']:
                return winner_heuristic(
                    side['1'],
                    side['2'],
                    run_history
                )
        else:
            winner_side_two = get_winner(
                side['2'], run_history
            )
            return winner_heuristic(
                side['1'],
                winner_side_two,
                run_history
            )
    else:
        winner_side_one = get_winner(
            side['1'], run_history
        )
        winner_side_two = get_winner(
            side['2'], run_history
        )
        return winner_heuristic(
            winner_side_one,
            winner_side_two,
            run_history
        )


class Bracket(object):

    def __init__(self, data):
        self.data = data

    def run(self):
        run_history = []
        winner = get_winner(
            self.data,
            run_history
        )
        import pdb
        pdb.set_trace()




