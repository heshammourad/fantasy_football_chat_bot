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
        'name': 'Work From Home Consultants',
        'emoji': 'ff-sparsh'
    },
    'YEAH': {
        'name': 'Georgia Flings',
        'emoji': 'ff-gaurav'
    }
}


def get_team(abbrev: str) -> str:
    return f':{get_team_emoji(abbrev)}: _{get_team_name(abbrev)}_'


def get_team_emoji(abbrev: str) -> str:
    return teams[abbrev]['emoji']


def get_team_name(abbrev: str) -> str:
    return teams[abbrev]['name']


def get_section_header(header):
    return [
        {'type': 'divider'},
        {'type': 'section', 'text': {'type': 'mrkdwn', 'text': f'*_{header}_*'}}
    ]


def get_mrkdwn_from_arr(arr):
    return {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': '\n'.join(arr)
        }
    }


def get_number_prefix(num):
    return str(num).split('.')[0]


def get_number_length(num):
    return len(get_number_prefix(num))


def format_number(num, target_length=1, decimal_places=0):
    formatted_number = f"{num:.{decimal_places}f}"
    padding_length = target_length - get_number_length(num)
    padding = ' ' * padding_length
    return padding + formatted_number


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

        medalists.append(f':{medal}_place_medal: *{format_number(value, leading_value_length,
                         decimal_places=decimal_places)}* - {get_team(team.team_abbrev)}')
    return medalists


def create_dict(keys, substructure):
    return {key: substructure.copy() for key in keys}
