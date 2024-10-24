from num2words import num2words


teams = {
    'CL': {
        'name': 'wut r sports',
        'emoji': 'ff-claire'
    },
    'FIG': {
        'name': 'IPA Drunk Monks',
        'emoji': 'ff-john'
    },
    'GOGA': {
        'name': 'Orlando Goga',
        'emoji': 'ff-murtaza'
    },
    'HM': {
        'name': 'Hesham Marauders',
        'emoji': 'ff-hesham'
    },
    'KTT': {
        'name': "Kim's Top-Notch Team",
        'emoji': 'ff-kim'
    },
    'LNU': {
        'name': 'Jigness LNU',
        'emoji': 'ff-shetu'
    },
    'RR': {
        'name': 'Roswell Raiders',
        'emoji': 'ff-ashwin'
    },
    'TIDE': {
        'name': 'Crimson Tide',
        'emoji': 'ff-vijay'
    },
    'WFH': {
        'name': 'Stay At Home Consultants',
        'emoji': 'ff-sparsh'
    },
    'YEAH': {
        'name': 'Georgia Flings',
        'emoji': 'ff-gaurav'
    }
}


def get_teams():
    return teams.keys()


def get_team(abbrev: str) -> str:
    return f':{get_team_emoji(abbrev)}: _{get_team_name(abbrev)}_'


def get_team_emoji(abbrev: str) -> str:
    return teams[abbrev]['emoji']


def get_team_name(abbrev: str) -> str:
    return teams[abbrev]['name']


def get_fields(fields):
    fields_block = []
    for i in range(0, len(fields), 2):
        fields_section = [get_mrkdwn_text(field) for field in fields[i:i + 2]]
        fields_block.append({
            'type': 'section',
            'fields': fields_section
        })
    return fields_block


def get_header(text):
    return {
        'type': 'header',
        'text': {
            'type': 'plain_text',
            'text': text
        }
    }


def get_section_header(header):
    return [
        {'type': 'divider'},
        {'type': 'section', 'text': {'type': 'mrkdwn', 'text': f'*_{header}_*'}}
    ]


def get_mrkdwn_text(text):
    return {
        'type': 'mrkdwn',
        'text': text
    }


def get_mrkdwn_from_arr(arr):
    text = '\n'.join(arr) if type(arr) is list else arr
    return {
        'type': 'section',
        'text': get_mrkdwn_text(text)
    }


def get_context_from_arr(arr):
    text = '\n'.join(arr) if type(arr) is list else arr
    return {
        "type": "context",
        "elements": [get_mrkdwn_text(text)]
    }


def get_formatted_scoreboard(away_team, away_score, home_team, home_score, is_final=False):
    away_score_text = format_number(away_score, target_length=3, decimal_places=2)
    home_score_text = format_number(home_score, target_length=3, decimal_places=2)
    if is_final:
        if away_score > home_score:
            away_score_text = f'*{away_score_text}*'
        else:
            home_score_text = f'*{home_score_text}*'
    scores = [(away_team, away_score_text), (home_team, home_score_text)]
    return '\n'.join([f'{x[1]}\t{get_team(x[0])}' for x in scores])


def get_number_prefix(num):
    return str(num).split('.')[0]


def get_number_length(num):
    return len(get_number_prefix(num))


def format_number(num, target_length=1, decimal_places=0):
    formatted_number = f"{num:.{decimal_places}f}"
    padding_length = target_length - get_number_length(num)
    padding = ' ' * padding_length
    return padding + formatted_number


def get_rank_ordinal(arr, value, reverse=True):
    def condition(n, value): return n > value if reverse else n < value
    return num2words(sum(1 for n in arr if condition(n, value)) + 1, to='ordinal_num')


medals = ['first', 'second', 'third']


def get_medalists(teams, field_getter, decimal_places=0):
    sorted_teams = sorted(teams, key=field_getter, reverse=True)
    medalists = []
    prev_medal = ''
    leading_value_length = get_number_length(field_getter(sorted_teams[0]))
    for i, team in enumerate(sorted_teams):
        value = field_getter(team)

        try:
            medal = prev_medal if i != 0 and value == field_getter(sorted_teams[i - 1]) else medals[i]
        except IndexError:
            break
        prev_medal = medal

        try:
            team_abbrev = team.team_abbrev
        except AttributeError:
            team_abbrev = team['team_abbrev']

        medalists.append(f':{medal}_place_medal: *{format_number(value, leading_value_length,
                         decimal_places=decimal_places)}* - {get_team(team_abbrev)}')
    return medalists


def is_starter(player):
    return player.lineupSlot not in ['BE', 'IR']
