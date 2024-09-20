import json
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


def get(league):
    leaderboards = [utils.get_header('Frivolities')]
    leaderboards.extend(get_leaderboards(league))
    leaderboards.extend(get_trophies(league.box_scores(league.current_week - 1)))
    return leaderboards


def get_leaderboards(league):
    for i in range(1, league.current_week):
        box_scores = league.box_scores(i)
        for box_score in box_scores:
            process(box_score.away_team.team_abbrev, box_score.away_lineup)
            process(box_score.home_team.team_abbrev, box_score.home_lineup)

    headings_fields = []
    leaderboards_fields = []
    for i, (category, data) in enumerate(positions.items()):
        medalists = utils.get_medalists([{'team_abbrev': team, **stats}
                                              for team, stats in teams.items()], lambda x: x[category], decimal_places=data['decimals'])
        headings_fields.append(generate_mrkdwn_text(f':{data['emoji']}: *{category}s*'))
        leaderboards_fields.append(generate_mrkdwn_text('\n'.join(medalists)))
    
    leaderboards_section = utils.get_section_header('Leaderboards')
    while len(headings_fields) > 0:
        headings_sections = headings_fields[0:2]
        headings_fields = headings_fields[2:]

        leaderboards_sections = leaderboards_fields[0:2]
        leaderboards_fields = leaderboards_fields[2:]

        leaderboards_section.extend(generate_fields_sections([headings_sections, leaderboards_sections]))

    return leaderboards_section


def process(team_abbrev, lineup):
    team = teams[team_abbrev]
    roster_breakdown = {pos: [] for pos in positions.keys() if positions[pos]['top'] > 0}
    for player in lineup:
        if player.lineupSlot in ['BE', 'IR']:
            continue
        stats = list(player.stats.values())[0]
        team['TD'] += sum(value for key, value in stats['breakdown'].items() if key in td_keys)

        roster_breakdown[player.position].append(player.points)

    for position, scores in roster_breakdown.items():
        sorted_scores = sorted(scores)
        counted_scores = sorted_scores[-positions[position]['top']:]
        team[position] += sum(counted_scores)

def get_trophies(box_scores):
    trophies_section = utils.get_section_header('Trophies')
    return trophies_section

def generate_mrkdwn_text(text):
    return {'type': 'mrkdwn', 'text': text}

def generate_fields_sections(sections):
    fields_sections = []
    for section in sections:
        fields_sections.append({
            'type': 'section',
            'fields': section
        })
    return fields_sections