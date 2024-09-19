import utils


def get(league):
    week = league.current_week - 1
    box_scores = league.box_scores(week=week)
    standings = league.standings()

    summary = [
        {
            'type': 'header',
            'text': {
                    'type': 'plain_text',
                    'text': f'Week {week} Recap'
            }
        }
    ]

    summary.extend(get_results(box_scores))
    summary.extend(get_standings(standings))
    summary.extend(get_prizes(standings, week))

    return summary


def get_results(box_scores):
    results = utils.get_section_header('Results')

    for score in box_scores:
        away_score = utils.format_number(score.away_score, target_length=3, decimal_places=2)
        home_score = utils.format_number(score.home_score, target_length=3, decimal_places=2)
        if score.away_score > score.home_score:
            away_score = f'*{away_score}*'
        else:
            home_score = f'*{home_score}*'

        scores = [(score.away_team.team_abbrev, away_score), (score.home_team.team_abbrev, home_score)]
        results.append(utils.get_mrkdwn_from_arr(map(lambda x: f'{x[1]}\t{utils.get_team(x[0])}', scores)))

    return results


def get_standings(standings):
    standings_section = utils.get_section_header('Standings')
    standings_section.extend([get_standings_section(standings, 0, 6), get_standings_section(standings, 6, 10)])
    return standings_section


def get_standings_section(standings, start, end):
    texts = []
    for i in range(start, end):
        team = standings[i]
        texts.append(f' {i + 1}. {utils.get_team(team.team_abbrev)} ({team.wins}-{team.losses})')
    return utils.get_mrkdwn_from_arr(texts)


def get_prizes(standings, current_week):
    prizes = utils.get_section_header('Prizes')
    prizes.extend(get_scoring_leaders(standings))
    prizes.extend(get_survivor(standings, current_week))
    prizes.extend(get_best_week(standings))
    return prizes


def get_scoring_leaders(standings):
    scoring_leaders = [{
        'type': 'section',
        'text': {
                'type': 'mrkdwn',
                'text': '*$10 Regular Season Scoring Leader*'
        }}]
    most_points = utils.get_medalists(standings, lambda x: x.points_for, 2)
    scoring_leaders.append(utils.get_mrkdwn_from_arr(most_points))
    return scoring_leaders


def get_survivor(standings, current_week):
    eliminated_teams = []
    for week in range(0, min(current_week, len(standings) - 1)):
        week_standings = sorted(standings, key=lambda x: x.scores[week])
        for team in week_standings:
            team_abbrev = team.team_abbrev

            elimination_check = [t for t in eliminated_teams if t['team'] == team_abbrev]
            if elimination_check:
                continue

            eliminated_teams.append({
                'team': team_abbrev,
                'score': team.scores[week],
                'week': week + 1
            })
            break

    survivor_sections = [{
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*$8 Survivor Tournament*'
        }
    }]

    top_scorers = sorted(standings, key=lambda x: x.points_for, reverse=True)
    surviving_teams = []
    for team in top_scorers:
        team_abbrev = team.team_abbrev
        elimination_check = [t for t in eliminated_teams if t['team'] == team_abbrev]
        if elimination_check:
            continue

        surviving_teams.append(team_abbrev)
    survivor_sections.append(utils.get_mrkdwn_from_arr(
        map(lambda x: f':muscle: - {utils.get_team(x)}', surviving_teams)))

    survivor_sections.append(utils.get_mrkdwn_from_arr(
        map(lambda x: f':skull: - {utils.get_team(x['team'])} (Week {x['week']}: {utils.format_number(x['score'], decimal_places=2)})', reversed(eliminated_teams))))

    return survivor_sections


def get_best_week(standings):
    best_score = 0
    best_team = ''
    best_week = 0
    for team in standings:
        for week, score in enumerate(team.scores):
            if score < best_score:
                continue
            best_score = score
            best_team = team.team_abbrev
            best_week = week + 1
    return [{
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '*$4 Highest Scoring Week*'
        }
    }, {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': f'*{utils.format_number(best_score, decimal_places=2)}* - {utils.get_team(best_team)} (Week {best_week})'
        }
    }]
