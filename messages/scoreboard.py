import datetime
import utils


def get(league):
    now = datetime.datetime.now()
    scoreboard = [utils.get_header(f'Week {league.current_week} Scoreboard')]

    box_scores = league.box_scores()
    for matchup in box_scores:
        away_score = matchup.away_score
        home_score = matchup.home_score
        scores = [utils.format_number(score, target_length=3, decimal_places=2)
                  for score in [away_score, home_score]]
        to_play = [sum(1 for player in lineup if utils.is_starter(player) and hasattr(player, 'game_date')
                       and player.game_date > now) for lineup in [matchup.away_lineup, matchup.home_lineup]]

        scoreboard.append({'type': 'divider'})
        scoreboard.append(utils.get_context_from_arr(get_breakdown(to_play[0], matchup.away_projected)))
        scoreboard.append(utils.get_mrkdwn_from_arr(utils.get_formatted_scoreboard(matchup.away_team.team_abbrev,
                          away_score, matchup.home_team.team_abbrev, home_score)))
        scoreboard.append(utils.get_context_from_arr(get_breakdown(to_play[1], matchup.home_projected)))

    return scoreboard


def get_breakdown(to_play, proj):
    return f'To Play: *{to_play}*\tProj Total: *{utils.format_number(proj, decimal_places=2)}*'
