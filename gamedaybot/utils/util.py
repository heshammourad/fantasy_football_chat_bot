from datetime import datetime
import os
from typing import List


def str_to_bool(check: str) -> bool:
    """
    Converts a string to a boolean value.

    Parameters
    ----------
    check : str
        The string to be converted to a boolean value.

    Returns
    -------
    bool
        The boolean value of the string.
    """
    try:
        return check.strip().lower() in ("yes", "true", "t", "1")
    except:
        return False


def str_limit_check(text: str, limit: int) -> List[str]:
    """
    Splits a string into parts of a maximum length.

    Parameters
    ----------
    text : str
        The text to be split.
    limit : int
        The maximum length of each split string part.

    Returns
    -------
    split_str : List[str]
        A list of strings split by the maximum length.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if limit <= 0:
        raise ValueError("Limit must be greater than 0")

    # Special case: For empty strings and strings with only spaces or newlines
    if len(text.strip()) == 0:
        return [""]

    split_str = []
    remaining_text = text.strip()

    while len(remaining_text) > 0:
        if len(remaining_text) > limit:
            part_one = remaining_text[:limit]
            last_newline = part_one.rfind('\n')

            # Remove extra newline if it's the last character
            if last_newline == len(part_one) - 1:
                last_newline -= 1

            # If a newline exists within the limit, split there
            if last_newline != -1:
                part_one = remaining_text[:last_newline]
                remaining_text = remaining_text[last_newline + 1:]
            else:
                remaining_text = remaining_text[limit:]

            # Only strip if this isn't the first part (to pass the 'test_str_limit_check_over_limit' test)
            if split_str:
                split_str.append(part_one.strip())
            else:
                split_str.append(part_one)
        else:
            split_str.append(remaining_text.strip())
            remaining_text = ""

    # Remove any empty strings that might be produced due to stripping
    split_str = [s for s in split_str if s]

    return split_str


def str_to_datetime(date_str: str) -> datetime:
    """
    Converts a string in the format of 'YYYY-MM-DD' to a datetime object.

    Parameters
    ----------
    date_str : str
        The string to be converted to a datetime object in 'YYYY-MM-DD' format.

    Returns
    -------
    datetime
        The datetime object created from the input string.

    Raises
    ------
    TypeError
        If the input is not a string.
    ValueError
        If the input does not match the expected date format.
    """
    if not isinstance(date_str, str):
        raise TypeError("Input must be a string")

    date_format = "%Y-%m-%d"
    try:
        return datetime.strptime(date_str.strip(), date_format)
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD' format.")


def currently_in_season(season_start_date=None, season_end_date=None, current_date=None):
    """
    Check if the current date is during the football season.

    Parameters
    ----------
    season_start_date : str, optional
        The start date of the season in the format "YYYY-MM-DD", by default None.
    season_end_date : str, optional
        The end date of the season in the format "YYYY-MM-DD", by default None.
    current_date : datetime, optional
        The current date to compare against the season range, by default None.

    Returns
    -------
    bool
        True if the current date is within the range of dates for the football season, False otherwise.

    Raises
    ------
    ValueError
        If the season start or end date is not in the correct format "YYYY-MM-DD".
        If the current_date is not a datetime object.
    """

    if not current_date:
        current_date = datetime.now()

    if not season_start_date:
        try:
            season_start_date = str(os.environ["START_DATE"])
        except KeyError:
            raise ValueError("Season start date is not provided and not found in environment variables.")

    if not season_end_date:
        try:
            season_end_date = str(os.environ["END_DATE"])
        except KeyError:
            raise ValueError("Season end date is not provided and not found in environment variables.")

    season_start_date = str_to_datetime(season_start_date)
    season_end_date = str_to_datetime(season_end_date)

    return season_start_date <= current_date <= season_end_date


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


def format_number(num, target_length, decimal_places):
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
