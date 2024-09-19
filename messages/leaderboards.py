import utils

positions = ['QB', 'RB', 'WR', 'TE', 'D/ST', 'K']
td_keys = ['defensivePlusSpecialTeamsTouchdowns', 'passingTouchdowns', 'receivingTouchdowns', 'rushingTouchdowns']
teams = utils.create_dict(utils.get_teams(),
                          {"TD": 0, "QB": 0, "RB": 0, "WR": 0, "TE": 0, "D/ST": 0, "K": 0})


def get(league):
    for i in range(1, league.current_week):
        box_scores = league.box_scores(i)
        for box_score in box_scores:
            process(box_score.away_team.team_abbrev, box_score.away_lineup)
            process(box_score.home_team.team_abbrev, box_score.home_lineup)
    print(teams)


def process(team, lineup):
    for player in lineup:
        if player.lineupSlot in ['BE', 'IR']:
            continue
        stats = list(player.stats.values())[0]
        teams[team]['TD'] += sum(value for key, value in stats['breakdown'].items() if key in td_keys)
