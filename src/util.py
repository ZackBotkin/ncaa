
def validate_side(side):
    not_base_case = ('team' not in side and 'seed' not in side)
    not_recursive_case = ('1' not in side and '2' not in side)
    if not_base_case and not_recursive_case:
        raise Exception("%s" % side)

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

def calculate_score(team, disable_chance=True):
    score = team['seed']
    if 'injured_list' in team:
        injured_list = team['injured_list']
        if len(injured_list) < 1:
            pass
        elif len(injured_list) < 3:
            score += 1
        elif len(injured_list) < 5:
            score += 2
        else:
            score += 3

    return score

def winner_heuristic(team_one, team_two, run_history):

    team_one_score = calculate_score(team_one)
    team_two_score = calculate_score(team_two)

    if team_one_score < team_two_score:
        run_history.append(
            '#%d %s defeats #%d %s' % (
                team_one['seed'],
                team_one['team'],
                team_two['seed'],
                team_two['team']
            )
        )
        return team_one
    else:
        run_history.append(
            '#%d %s defeats #%d %s' % (
                team_two['seed'],
                team_two['team'],
                team_one['seed'],
                team_one['team']
            )
        )
        return team_two
