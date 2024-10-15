import gamedaybot.espn.functionality as functionality
import utils

positions = {
    'QB': {'top': 1, 'decimals': 2, 'emoji': 'quarter'},
    'RB': {'top': 2, 'decimals': 1, 'emoji': 'runner'},
    'WR': {'top': 3, 'decimals': 1, 'emoji': 'gloves'},
    'TE': {'top': 1, 'decimals': 1, 'emoji': 'link'},
    'D/ST': {'top': 1, 'decimals': 0, 'emoji': 'shield'},
    'K': {'top': 1, 'decimals': 1, 'emoji': 'athletic_shoe'},
    'TD': {'top': 0, 'decimals': 0, 'emoji': 'football'}
}
td_keys = ['defensivePlusSpecialTeamsTouchdowns', 'passingTouchdowns', 'receivingTouchdowns', 'rushingTouchdowns']
teams = {team: {category: 0 for category in list(positions.keys()) + ['TD']} for team in utils.get_teams()}
trophies = [
    ('High Score', 'fire'), ('Low Score', 'ice_cube'),
    ('Blowout', 'sunglasses'), ('Squeaker', 'sweat_smile'),
    ('Lucky', 'four_leaf_clover'), ('Unlucky', 'rage'),
    ('Overachiever', 'chart_with_upwards_trend'), ('Underachiever', 'chart_with_downwards_trend'),
    ('Best Manager', 'white_check_mark'), ('Worst Manager', 'x'),
    ('Stud', '+1'), ('Dud', '-1'),
    ('Benchwarmer', 'dotted_fire')
]


def get(league):
    leaderboards = [utils.get_header('Superlatives')]
    leaderboards.extend(get_leaderboards(league))
    leaderboards.extend(get_trophies(league))
    return leaderboards


def get_leaderboards(league):
    for i in range(1, league.current_week):
        box_scores = league.box_scores(i)
        for box_score in box_scores:
            process(box_score.away_team.team_abbrev, box_score.away_lineup)
            process(box_score.home_team.team_abbrev, box_score.home_lineup)

    leaderboards_section = utils.get_section_header('Leaderboards')
    for i, (category, data) in enumerate(positions.items()):
        medalists = utils.get_medalists([{'team_abbrev': team, **stats}
                                         for team, stats in teams.items()], lambda x: x[category], decimal_places=data['decimals'])
        leaderboards_section.append(utils.get_mrkdwn_from_arr(f':{data['emoji']}: *{category}s*'))
        leaderboards_section.append(utils.get_context_from_arr(medalists))

    return leaderboards_section


def process(team_abbrev, lineup):
    team = teams[team_abbrev]
    roster_breakdown = {pos: [] for pos in positions.keys() if positions[pos]['top'] > 0}
    for player in lineup:
        if not utils.is_starter(player):
            continue
        stats = list(player.stats.values())[0]
        team['TD'] += sum(value for key, value in stats['breakdown'].items() if key in td_keys)

        roster_breakdown[player.position].append(player.points)

    for position, scores in roster_breakdown.items():
        sorted_scores = sorted(scores)
        counted_scores = sorted_scores[-positions[position]['top']:]
        team[position] += sum(counted_scores)


def get_trophies(league):
    box_scores = league.box_scores(league.current_week - 1)

    functionality.optimal_team_scores(league, full_report=True)

    trophies_section = utils.get_section_header('Trophies')

    scores = []
    results = []
    performances = []
    players = []
    benchwarmers = []

    for box_score in box_scores:
        away_team = box_score.away_team.team_abbrev
        away_score = box_score.away_score
        home_team = box_score.home_team.team_abbrev
        home_score = box_score.home_score
        scores.extend([(away_team, away_score), (home_team, home_score)])

        if (away_score > home_score):
            results.append((away_team, home_team, away_score, home_score))
        else:
            results.append((home_team, away_team, home_score, away_score))

        away_performance = away_score - box_score.away_projected
        home_performance = home_score - box_score.home_projected
        performances.extend([(away_team, away_performance), (home_team, home_performance)])

        players.extend([(away_team, p, away_score - home_score) for p in get_active_players(box_score.away_lineup)])
        players.extend([(home_team, p, home_score - away_score) for p in get_active_players(box_score.home_lineup)])

        benchwarmers.extend([(away_team, combo) for combo in get_benchwarmers(box_score.away_lineup)])
        benchwarmers.extend([(home_team, combo) for combo in get_benchwarmers(box_score.home_lineup)])

    trophies_values = []

    # High and Low Scores
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    high_score, low_score = sorted_scores[0], sorted_scores[-1]
    trophies_values.append(
        f'{utils.get_team(high_score[0])} led the league with *{utils.format_number(high_score[1], decimal_places=2)}* points')
    trophies_values.append(
        f'{utils.get_team(low_score[0])} had the lowest score with *{utils.format_number(low_score[1], decimal_places=2)}* points')

    # Blowout and Squeaker
    sorted_results = sorted(results, key=lambda x: abs(x[2] - x[3]), reverse=True)
    blowout, squeaker = sorted_results[0], sorted_results[-1]
    trophies_values.append(f'{utils.get_team(blowout[0])} blew out {utils.get_team(blowout[1])} by *{utils.format_number(
        blowout[2] - blowout[3], decimal_places=2)}* points ({utils.format_number(blowout[2], decimal_places=2)}-{utils.format_number(blowout[3], decimal_places=2)})')
    trophies_values.append(f'{utils.get_team(squeaker[1])} lost to {utils.get_team(squeaker[0])} by *{utils.format_number(
        squeaker[2] - squeaker[3], decimal_places=2)}* points ({utils.format_number(squeaker[2], decimal_places=2)}-{utils.format_number(squeaker[3], decimal_places=2)})')

    # Lucky and Unlucky
    points = sorted([score for sublist in [result[2:4] for result in results] for score in sublist])
    sorted_lucky = sorted(results, key=lambda x: x[2])
    lucky_rank = utils.get_rank_ordinal(points, sorted_lucky[0][2], reverse=True)
    trophies_values.append(f'{utils.get_team(sorted_lucky[0][0])} finished with the {
                           lucky_rank} highest score, but still came away with the win')

    sorted_unlucky = sorted(results, key=lambda x: x[3], reverse=True)
    unlucky_rank = utils.get_rank_ordinal(points, sorted_unlucky[0][3])
    trophies_values.append(f'{utils.get_team(sorted_unlucky[0][1])} had the {
                           unlucky_rank} highest score, but still ended up taking the L')

    # Overachiever and Underachiever
    sorted_performances = sorted(performances, key=lambda x: x[1], reverse=True)
    overachiever, underachiever = sorted_performances[0], sorted_performances[-1]
    trophies_values.append(f'{utils.get_team(
        overachiever[0])} were over their projection by *{utils.format_number(abs(overachiever[1]), decimal_places=2)}* points')
    trophies_values.append(f'{utils.get_team(
        underachiever[0])} were under their projection by *{utils.format_number(abs(underachiever[1]), decimal_places=2)}* points')

    # Best and Worst Managers
    accuracy = list(functionality.optimal_team_scores(league, full_report=True).items())
    best, worst = accuracy[0], accuracy[-1]
    trophies_values.append(f'{utils.get_team(
        best[0].team_abbrev)} scored *{utils.format_number(best[1][3], decimal_places=1)}%* of their optimal score')
    trophies_values.append(f'{utils.get_team(worst[0].team_abbrev)} left {utils.format_number(
        worst[1][2], decimal_places=2)} points on the bench, scoring only *{utils.format_number(worst[1][3], decimal_places=1)}%* of their optimal score')

    # Studs and Duds
    player_achievement = sorted([p for p in players], key=lambda x: x[1].points - x[1].projected_points, reverse=True)
    studs = search_players(player_achievement, condition=lambda x: x[2] > 0 and x[1].points -
                           x[1].projected_points > x[2], sort=lambda x: x[1].points - x[1].projected_points - x[2], reverse=True)
    stud = studs[0] if studs else player_achievement[0]
    stud_text = f'*{stud[1].name}* - {utils.get_team(stud[0])} outperformed projection by *{
        utils.format_number(stud[1].points - stud[1].projected_points, decimal_places=2)}*'
    if studs:
        stud_text += f' in a {utils.format_number(stud[2], decimal_places=2)} win'
    trophies_values.append(stud_text)

    duds = search_players(player_achievement, condition=lambda x: x[2] < 0 and x[1].points -
                          x[1].projected_points < x[2], sort=lambda x: x[1].points - x[1].projected_points - x[2])
    dud = duds[0] if duds else player_achievement[-1]
    dud_text = f'*{dud[1].name}* - {utils.get_team(dud[0])} underperformed projection by *{
        utils.format_number(dud[1].projected_points - dud[1].points, decimal_places=2)}*'
    if duds:
        dud_text += f' in a {utils.format_number(abs(dud[2]), decimal_places=2)} loss'
    trophies_values.append(dud_text)

    # Benchwarmer
    sorted_benchwarmers = sorted(benchwarmers, key=lambda x: x[1][1].points - x[1][0].points, reverse=True)
    benchwarmer_team, (starter, benchwarmer) = sorted_benchwarmers[0]
    trophies_values.append(f'*{benchwarmer.name}* - {utils.get_team(benchwarmer_team)} scored *{utils.format_number(benchwarmer.points, decimal_places=positions[benchwarmer.position]['decimals'])}* points on the bench while {
                           starter.name} scored just {utils.format_number(starter.points, decimal_places=positions[starter.position]['decimals'])}')

    trophies_headers = [f':{emoji}: *{name}*' for (name, emoji) in trophies]
    for i, header in enumerate(trophies_headers):
        trophies_section.append(utils.get_mrkdwn_from_arr(header))
        trophies_section.append(utils.get_context_from_arr(trophies_values[i]))

    return trophies_section


def get_benchwarmers(lineup):
    benchwarmers = []
    active_players = get_active_players(lineup)
    for player in get_bench_players(lineup):
        possible_positions = set([p.position for p in active_players if p.lineupSlot in player.eligibleSlots])
        possible_replacements = [p for p in active_players if p.position in possible_positions]
        benchwarmers.extend([(starter, player) for starter in possible_replacements])
    return benchwarmers


def get_active_players(lineup):
    return search_players(lineup, condition=lambda x: utils.is_starter(x))


def get_bench_players(lineup):
    return search_players(lineup, condition=lambda x: x.lineupSlot == 'BE')


def search_players(players, condition=None, sort=None, reverse=False):
    filtered_players = [p for p in players if condition(p)]
    if not sort:
        return filtered_players
    return sorted(filtered_players, key=sort, reverse=reverse)
