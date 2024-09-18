import json
import utils.util as util


def get_standings_section(standings, start, end):
    texts = []
    for i in range(start, end):
        team = standings[i]
        texts.append(f' {i + 1}. {util.get_team(team.team_abbrev)} ({team.wins}-{team.losses})')
    return util.get_mrkdwn_from_arr(texts)


def get(league):
    week = league.current_week - 1
    box_scores = league.box_scores(week=week)

    summary = {
        'blocks': [
            {
                'type': 'header',
                'text': {
                    'type': 'plain_text',
                    'text': f'Week {week} Recap'
                }
            },
            {
                'type': 'divider'
            },
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': '*_Results_*'
                }
            }
        ]
    }

    for score in box_scores:
        away_score = score.away_score
        if away_score < 100:
            away_score = f' {away_score}'
        home_score = score.home_score
        if home_score < 100:
            away_score = f' {home_score}'

        if score.away_score > score.home_score:
            away_score = f'*{away_score}*'
        else:
            home_score = f'*{home_score}*'

        away = f'{away_score}\t{util.get_team(score.away_team.team_abbrev)}'
        home = f'{home_score}\t{util.get_team(score.home_team.team_abbrev)}'

        summary['blocks'].append({
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': f'{away}\n{home}'
            }
        })

    summary['blocks'].extend([
        {
            'type': 'divider'
        },
        {
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': '*_Standings_*'
            }
        }
    ])

    standings = league.standings()
    summary['blocks'].extend([get_standings_section(standings, 0, 6), get_standings_section(standings, 6, 10)])

    summary['blocks'].extend([
        {
            'type': 'divider'
        },
        {
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': '*_Prizes_*'
            }
        },
        {
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': '*$10 Regular Season Scoring Leader*'
            }
        }
    ])

    most_points = util.get_medalists(standings, lambda x: x.points_for, 2)
    summary['blocks'].append(util.get_mrkdwn_from_arr(most_points))

    return json.dumps(summary, indent=2)
