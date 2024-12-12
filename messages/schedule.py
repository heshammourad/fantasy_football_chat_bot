import utils

prev_history = [
    (2019, '1', 'RR', 'FIG', 127.4, 78.92),
    (2019, '1', 'TIDE', 'YEAH', 165.54, 130.32),
    (2019, '2', 'HM', 'RR', 142.02, 94.26),
    (2019, '2', 'WFH', 'GOGA', 127.24, 101.96),
    (2019, '2', 'FIG', 'TIDE', 123.72, 111.56),
    (2019, '3', 'YEAH', 'RR', 166.34, 71.14),
    (2019, '3', 'FIG', 'HM', 122.06, 109.02),
    (2019, '3', 'GOGA', 'KTT', 128.08, 123.26),
    (2019, '4', 'HM', 'YEAH', 132.08, 92.8),
    (2019, '4', 'RR', 'TIDE', 96.62, 96.4),
    (2019, '5', 'YEAH', 'FIG', 130.24, 101.44),
    (2019, '5', 'WFH', 'KTT', 130.12, 101.76),
    (2019, '5', 'TIDE', 'HM', 192.82, 175.1),
    (2019, '6', 'FIG', 'GOGA', 129.22, 103.44),
    (2019, '6', 'WFH', 'TIDE', 101.52, 87.76),
    (2019, '6', 'HM', 'KTT', 112.72, 109.84),
    (2019, '7', 'GOGA', 'YEAH', 114.72, 61.72),
    (2019, '7', 'TIDE', 'KTT', 121.26, 80.94),
    (2019, '7', 'RR', 'WFH', 110.56, 108.76),
    (2019, '8', 'WFH', 'FIG', 159.7, 78.94),
    (2019, '8', 'KTT', 'RR', 138.48, 113.7),
    (2019, '9', 'GOGA', 'HM', 128.72, 93.5),
    (2019, '9', 'KTT', 'FIG', 141.06, 112.84),
    (2019, '9', 'YEAH', 'WFH', 119.24, 93.54),
    (2019, '10', 'KTT', 'YEAH', 123.52, 105.72),
    (2019, '10', 'TIDE', 'GOGA', 147.94, 139.92),
    (2019, '11', 'GOGA', 'RR', 133.88, 92.46),
    (2019, '11', 'WFH', 'HM', 124.88, 114.82),
    (2019, '12', 'TIDE', 'WFH', 142.76, 105.98),
    (2019, '12', 'HM', 'KTT', 124.32, 92.84),
    (2019, '12', 'GOGA', 'FIG', 98.76, 95.48),
    (2019, '13', 'KTT', 'RR', 120.1, 94.9),
    (2019, 'QF', 'HM', 'WFH', 113.82, 96.26),
    (2019, 'SF', 'TIDE', 'GOGA', 131.24, 88.2),
    (2019, '14', 'YEAH', 'KTT', 118.28, 100.5),
    (2019, '15', 'RR', 'YEAH', 139.18, 117.92),
    (2019, 'F', 'TIDE', 'HM', 153.96, 152.72),
    (2020, '1', 'YEAH', 'WFH', 100.1, 62.44),
    (2020, '1', 'RR', 'CL', 103.04, 89.3),
    (2020, '1', 'HM', 'FIG', 95.82, 86.52),
    (2020, '2', 'TIDE', 'FIG', 126.18, 77.7),
    (2020, '2', 'WFH', 'RR', 89, 72.68),
    (2020, '3', 'KTT', 'YEAH', 104.04, 46.02),
    (2020, '3', 'HM', 'GOGA', 103.2, 58.28),
    (2020, '4', 'HM', 'TIDE', 121.34, 72.9),
    (2020, '4', 'CL', 'GOGA', 103.9, 66.72),
    (2020, '4', 'KTT', 'RR', 97.72, 90.24),
    (2020, '5', 'CL', 'WFH', 125.1, 77.94),
    (2020, '5', 'GOGA', 'TIDE', 106.5, 71.66),
    (2020, '5', 'FIG', 'YEAH', 91.88, 68.24),
    (2020, '6', 'FIG', 'RR', 92.5, 85),
    (2020, '6', 'WFH', 'GOGA', 105.72, 101.34),
    (2020, '7', 'HM', 'YEAH', 104.72, 93.02),
    (2020, '7', 'CL', 'KTT', 101.86, 97.48),
    (2020, '8', 'RR', 'HM', 95.14, 78.94),
    (2020, '8', 'WFH', 'KTT', 90.9, 79.06),
    (2020, '8', 'TIDE', 'YEAH', 69.16, 66.64),
    (2020, '9', 'TIDE', 'RR', 97.86, 80.48),
    (2020, '9', 'CL', 'FIG', 94.18, 92.84),
    (2020, '10', 'KTT', 'GOGA', 129.26, 70.86),
    (2020, '10', 'FIG', 'WFH', 71.42, 65.08),
    (2020, '11', 'GOGA', 'YEAH', 88.34, 73.28),
    (2020, '11', 'CL', 'HM', 107.24, 93.02),
    (2020, '12', 'TIDE', 'CL', 136.28, 90.5),
    (2020, '12', 'WFH', 'HM', 114.58, 78.12),
    (2020, '12', 'YEAH', 'RR', 83.8, 77.36),
    (2020, '12', 'FIG', 'KTT', 105.12, 104.3),
    (2020, '13', 'RR', 'GOGA', 81.26, 45.08),
    (2020, '13', 'WFH', 'TIDE', 101.7, 86.92),
    (2020, '14', 'TIDE', 'YEAH', 126.82, 68.96),
    (2020, 'QF', 'FIG', 'HM', 90.76, 88.84),
    (2020, '15', 'CL', 'RR', 118.12, 83.96),
    (2020, '15', 'TIDE', 'WFH', 122.46, 96.64),
    (2020, '16', 'YEAH', 'WFH', 130.6, 83.14),
    (2020, '16', 'RR', 'HM', 101.04, 67.88),
    (2021, '1', 'WFH', 'GOGA', 133.66, 70.96),
    (2021, '1', 'TIDE', 'RR', 131.7, 125.92),
    (2021, '2', 'KTT', 'YEAH', 107.8, 65.18),
    (2021, '2', 'GOGA', 'RR', 129.12, 103.18),
    (2021, '2', 'CL', 'WFH', 122.42, 116.4),
    (2021, '3', 'RR', 'CL', 79.32, 75.78),
    (2021, '3', 'WFH', 'FIG', 104.54, 101.42),
    (2021, '3', 'HM', 'KTT', 127.72, 126.54),
    (2021, '4', 'FIG', 'RR', 127.92, 78.22),
    (2021, '4', 'KTT', 'TIDE', 130.18, 80.54),
    (2021, '4', 'YEAH', 'HM', 103.42, 91.9),
    (2021, '5', 'TIDE', 'HM', 147.48, 128.7),
    (2021, '5', 'GOGA', 'KTT', 137.08, 126.52),
    (2021, '6', 'HM', 'GOGA', 150.54, 75.36),
    (2021, '6', 'TIDE', 'YEAH', 136.68, 111.84),
    (2021, '6', 'KTT', 'CL', 111.7, 92.3),
    (2021, '7', 'WFH', 'YEAH', 137.34, 86.54),
    (2021, '7', 'FIG', 'KTT', 114.34, 87.74),
    (2021, '7', 'GOGA', 'TIDE', 99.38, 89.78),
    (2021, '7', 'HM', 'CL', 105.36, 104.24),
    (2021, '8', 'WFH', 'RR', 114.56, 91.2),
    (2021, '8', 'FIG', 'HM', 112.56, 89.7),
    (2021, '8', 'GOGA', 'YEAH', 92.6, 73.76),
    (2021, '8', 'TIDE', 'CL', 95.54, 80.42),
    (2021, '9', 'RR', 'YEAH', 77.28, 53.7),
    (2021, '9', 'TIDE', 'FIG', 96.84, 89.36),
    (2021, '9', 'CL', 'GOGA', 100.54, 99.02),
    (2021, '10', 'FIG', 'GOGA', 93.24, 74.98),
    (2021, '10', 'CL', 'YEAH', 86.6, 83.46),
    (2021, '11', 'CL', 'FIG', 146.58, 70.26),
    (2021, '11', 'WFH', 'KTT', 140.58, 129.88),
    (2021, '12', 'FIG', 'YEAH', 119.7, 80.92),
    (2021, '12', 'WFH', 'HM', 148.58, 111.44),
    (2021, '12', 'KTT', 'RR', 109.96, 90.9),
    (2021, '13', 'HM', 'RR', 127.1, 73.42),
    (2021, '13', 'WFH', 'TIDE', 138.22, 105.72),
    (2021, '14', 'WFH', 'GOGA', 110.42, 64.7),
    (2021, '14', 'RR', 'TIDE', 131.04, 97.08),
    (2021, 'QF', 'WFH', 'TIDE', 147.28, 56.72),
    (2021, 'QF', 'CL', 'HM', 93.04, 84.16),
    (2021, 'SF', 'WFH', 'CL', 130.9, 80.34),
    (2021, '16', 'YEAH', 'GOGA', 94.2, 59.7),
    (2021, 'SF', 'FIG', 'KTT', 120.18, 96.56),
    (2021, '17', 'CL', 'KTT', 127.24, 73.06),
    (2021, '17', 'TIDE', 'HM', 103.42, 88.56),
    (2021, 'F', 'FIG', 'WFH', 113.5, 107.32),
    (2022, '1', 'RR', 'KTT', 135.52, 98.52),
    (2022, '1', 'HM', 'WFH', 133.68, 126.96),
    (2022, '1', 'LNU', 'YEAH', 93.96, 90.22),
    (2022, '1', 'FIG', 'CL', 114.3, 110.72),
    (2022, '2', 'HM', 'FIG', 96.84, 61.4),
    (2022, '2', 'TIDE', 'YEAH', 148.38, 118.22),
    (2022, '2', 'LNU', 'KTT', 71.98, 62.26),
    (2022, '2', 'RR', 'GOGA', 122.52, 117.96),
    (2022, '3', 'GOGA', 'LNU', 95.94, 57.44),
    (2022, '3', 'YEAH', 'KTT', 129.6, 104.1),
    (2022, '3', 'TIDE', 'CL', 119.5, 94.86),
    (2022, '3', 'RR', 'WFH', 119.32, 100.06),
    (2022, '4', 'GOGA', 'YEAH', 123.3, 105.26),
    (2022, '4', 'HM', 'CL', 95.02, 76.98),
    (2022, '4', 'TIDE', 'KTT', 114.52, 99.98),
    (2022, '4', 'LNU', 'WFH', 130.9, 118.1),
    (2022, '4', 'RR', 'FIG', 112.46, 111.16),
    (2022, '5', 'YEAH', 'WFH', 135.56, 82.32),
    (2022, '5', 'TIDE', 'HM', 148.06, 105.84),
    (2022, '5', 'LNU', 'FIG', 138.88, 99.18),
    (2022, '5', 'GOGA', 'KTT', 89, 73.28),
    (2022, '6', 'KTT', 'WFH', 136.5, 97.62),
    (2022, '6', 'TIDE', 'GOGA', 90.76, 59.82),
    (2022, '6', 'YEAH', 'FIG', 72.9, 67.52),
    (2022, '6', 'RR', 'CL', 97.5, 94.88),
    (2022, '7', 'CL', 'LNU', 127.06, 76.7),
    (2022, '7', 'WFH', 'GOGA', 101.32, 70.84),
    (2022, '7', 'RR', 'HM', 106.3, 85.52),
    (2022, '7', 'KTT', 'FIG', 108.54, 92.32),
    (2022, '8', 'LNU', 'HM', 115.88, 91.48),
    (2022, '8', 'TIDE', 'WFH', 129.72, 118.66),
    (2022, '8', 'GOGA', 'FIG', 95.24, 85.16),
    (2022, '8', 'CL', 'YEAH', 117.44, 111.08),
    (2022, '9', 'RR', 'TIDE', 161.12, 114.8),
    (2022, '9', 'CL', 'KTT', 88.5, 71.44),
    (2022, '9', 'YEAH', 'HM', 97.54, 83.4),
    (2022, '9', 'FIG', 'WFH', 123.24, 111),
    (2022, '10', 'GOGA', 'CL', 112.4, 66),
    (2022, '10', 'HM', 'KTT', 128.48, 92.28),
    (2022, '10', 'RR', 'LNU', 112.76, 103.6),
    (2022, '10', 'FIG', 'TIDE', 89.04, 83.8),
    (2022, '11', 'WFH', 'CL', 130.4, 101.54),
    (2022, '11', 'GOGA', 'HM', 96.84, 77.5),
    (2022, '11', 'TIDE', 'LNU', 123.34, 105.74),
    (2022, '11', 'YEAH', 'RR', 92.16, 87.96),
    (2022, '12', 'YEAH', 'LNU', 139.32, 116.36),
    (2022, '12', 'FIG', 'CL', 120.4, 105.14),
    (2022, '12', 'WFH', 'HM', 114.06, 104.18),
    (2022, '12', 'RR', 'KTT', 83.16, 81.6),
    (2022, '13', 'GOGA', 'RR', 117, 93.94),
    (2022, '13', 'LNU', 'KTT', 107.58, 102.84),
    (2022, '13', 'FIG', 'HM', 77.52, 74.74),
    (2022, '13', 'YEAH', 'TIDE', 90.9, 88.22),
    (2022, '14', 'TIDE', 'CL', 99.28, 60.26),
    (2022, '14', 'YEAH', 'KTT', 96.98, 62.06),
    (2022, '14', 'LNU', 'GOGA', 122.06, 100.1),
    (2022, '14', 'RR', 'WFH', 93.52, 91.18),
    (2022, 'QF', 'TIDE', 'FIG', 131.66, 99.64),
    (2022, 'QF', 'RR', 'GOGA', 106.12, 85.46),
    (2022, 'QF', 'YEAH', 'LNU', 122.4, 110.34),
    (2022, '15', 'CL', 'KTT', 109.98, 108.6),
    (2022, '15', 'WFH', 'HM', 101.02, 99.9),
    (2022, 'SF', 'RR', 'YEAH', 87.76, 44.6),
    (2022, '16', 'GOGA', 'FIG', 107.3, 103.36),
    (2022, '16', 'WFH', 'CL', 72.6, 69.68),
    (2022, '16', 'KTT', 'HM', 103.7, 101.26),
    (2022, '17', 'WFH', 'KTT', 96.48, 46.7),
    (2022, 'F', 'RR', 'TIDE', 114.78, 92.8),
    (2022, '17', 'CL', 'HM', 69.66, 66.2),
    (2022, '17', 'FIG', 'LNU', 96.02, 93.52),
    (2023, '1', 'FIG', 'WFH', 130.36, 69.08),
    (2023, '1', 'LNU', 'YEAH', 140.62, 100.56),
    (2023, '1', 'HM', 'GOGA', 134.34, 112.76),
    (2023, '1', 'TIDE', 'RR', 144.08, 129.58),
    (2023, '2', 'GOGA', 'CL', 179.3, 123.8),
    (2023, '2', 'HM', 'RR', 141.56, 106.98),
    (2023, '2', 'TIDE', 'WFH', 140.6, 132.92),
    (2023, '2', 'YEAH', 'FIG', 130.02, 125.98),
    (2023, '3', 'WFH', 'YEAH', 153.84, 118.6),
    (2023, '3', 'CL', 'RR', 167.96, 150.52),
    (2023, '3', 'TIDE', 'HM', 162.8, 146.1),
    (2023, '3', 'GOGA', 'LNU', 134.58, 122.46),
    (2023, '4', 'LNU', 'RR', 166.72, 96.2),
    (2023, '4', 'HM', 'CL', 159.16, 113.34),
    (2023, '4', 'YEAH', 'TIDE', 117.12, 107.04),
    (2023, '4', 'FIG', 'GOGA', 124.28, 114.28),
    (2023, '5', 'HM', 'LNU', 175.1, 133.4),
    (2023, '5', 'GOGA', 'WFH', 134.84, 107.82),
    (2023, '5', 'CL', 'TIDE', 146.3, 126.56),
    (2023, '5', 'RR', 'FIG', 149.04, 131.02),
    (2023, '6', 'CL', 'LNU', 137.28, 97.76),
    (2023, '6', 'HM', 'FIG', 128.32, 105.2),
    (2023, '6', 'RR', 'WFH', 133.86, 111.6),
    (2023, '6', 'YEAH', 'GOGA', 126.16, 104.94),
    (2023, '7', 'WFH', 'HM', 179.48, 130.16),
    (2023, '7', 'CL', 'FIG', 149.4, 118.32),
    (2023, '7', 'TIDE', 'LNU', 127.98, 110.26),
    (2023, '7', 'YEAH', 'RR', 130.3, 119.8),
    (2023, '8', 'WFH', 'CL', 144.44, 99.88),
    (2023, '8', 'LNU', 'FIG', 151.94, 128.88),
    (2023, '8', 'YEAH', 'HM', 138.32, 126.08),
    (2023, '8', 'GOGA', 'TIDE', 154.86, 153.9),
    (2023, '9', 'RR', 'GOGA', 108.92, 77.62),
    (2023, '9', 'YEAH', 'CL', 126.96, 96.9),
    (2023, '9', 'WFH', 'LNU', 132.06, 124.14),
    (2023, '9', 'FIG', 'TIDE', 110.8, 107.62),
    (2023, '10', 'YEAH', 'FIG', 143.66, 104.96),
    (2023, '10', 'WFH', 'HM', 179.18, 143.18),
    (2023, '10', 'GOGA', 'RR', 138.24, 110.78),
    (2023, '10', 'LNU', 'CL', 129.2, 103.1),
    (2023, '11', 'GOGA', 'CL', 148.52, 99.64),
    (2023, '11', 'HM', 'YEAH', 122.16, 113.74),
    (2023, '11', 'WFH', 'TIDE', 134.72, 127.04),
    (2023, '11', 'FIG', 'LNU', 132.8, 126.84),
    (2023, '12', 'LNU', 'HM', 215.64, 170.18),
    (2023, '12', 'WFH', 'RR', 135.82, 104.56),
    (2023, '12', 'YEAH', 'TIDE', 133.94, 108.52),
    (2023, '12', 'FIG', 'CL', 122.66, 115.66),
    (2023, '13', 'RR', 'TIDE', 137.86, 97.9),
    (2023, '13', 'LNU', 'YEAH', 166.66, 132.32),
    (2023, '13', 'WFH', 'GOGA', 134.44, 105.46),
    (2023, '13', 'HM', 'CL', 116.6, 110),
    (2023, '14', 'CL', 'YEAH', 139.2, 96.12),
    (2023, '14', 'FIG', 'HM', 158.98, 125.6),
    (2023, '14', 'GOGA', 'TIDE', 134.02, 102.72),
    (2023, '14', 'LNU', 'RR', 126.06, 115.04),
    (2023, '15', 'TIDE', 'RR', 140.36, 74.1),
    (2023, 'QF', 'GOGA', 'YEAH', 160.38, 111.1),
    (2023, 'QF', 'FIG', 'LNU', 136.62, 132.68),
    (2023, '16', 'YEAH', 'LNU', 178.02, 127.1),
    (2023, '16', 'CL', 'TIDE', 150.92, 108.22),
    (2023, 'SF', 'WFH', 'FIG', 142.7, 122.04),
    (2023, 'SF', 'HM', 'GOGA', 148.04, 131.3),
    (2023, 'F', 'WFH', 'HM', 176.84, 147.7),
    (2023, '17', 'LNU', 'YEAH', 144.6, 116.56),
    (2023, '17', 'GOGA', 'FIG', 102.38, 86.58),
    (2023, '17', 'TIDE', 'RR', 116.28, 110.92)
]


def get(league):
    week = league.current_week
    matchups = league.box_scores()
    schedule = [utils.get_header(f'Week {week} Schedule')]
    schedule.append({'type': 'divider'})

    history = list(prev_history)

    for wk in range(1, week):
        week_matchups = league.box_scores(week=wk)
        for matchup in week_matchups:
            away_abbrev = matchup.away_team.team_abbrev
            away_score = matchup.away_score
            home_abbrev = matchup.home_team.team_abbrev
            home_score = matchup.home_score

            if away_score > home_score:
                winner, loser = away_abbrev, home_abbrev
                win_score, lose_score = away_score, home_score
            else:
                winner, loser = home_abbrev, away_abbrev
                win_score, lose_score = home_score, away_score
            history.append((2024, str(wk), winner, loser, win_score, lose_score))

    for matchup in matchups:
        away_team = matchup.away_team
        if away_team == 0:
            continue
        home_team = matchup.home_team
        away_abbrev = away_team.team_abbrev
        home_abbrev = home_team.team_abbrev
        schedule.append(utils.get_mrkdwn_from_arr(f'{utils.get_team(away_abbrev)} {
                        get_record(away_team)} v {utils.get_team(home_abbrev)} {get_record(home_team)}'))

        matchup_teams = [away_abbrev, home_abbrev]
        h2h_wins = [0, 0]
        streak = ['', 0]
        last = ()
        for history_match in history:
            winner, loser = history_match[2:4]
            if set([winner, loser]) != set(matchup_teams):
                continue
            if winner == away_abbrev:
                h2h_wins[0] += 1
            else:
                h2h_wins[1] += 1

            if streak[0] == winner:
                streak[1] += 1
            else:
                streak = [winner, 1]

            last = history_match

        leading_team = None
        if h2h_wins[0] > h2h_wins[1]:
            leading_team = away_abbrev
        elif h2h_wins[1] > h2h_wins[0]:
            leading_team = home_abbrev
        h2h_text = 'tied' if h2h_wins[0] == h2h_wins[1] else f'{utils.get_team_name(leading_team)} leads'

        year, wk, winner, loser, win_score, lose_score = last
        week_text = 'Week ' if wk.isdigit() else ''
        breakdown_text = [
            f' ⚔️ *H2H*: {h2h_text} *{max(h2h_wins)}*-*{min(h2h_wins)}*',
            f' 🌠 *Streak*: {utils.get_team_name(streak[0])} - *W{streak[1]}*',
            f' ⏮️ *Last*: {year} {week_text}{wk} - {utils.get_team_name(winner)} *{utils.format_number(win_score, decimal_places=2)}*-*{
                utils.format_number(lose_score, decimal_places=2)}* {utils.get_team_name(loser)}',
            f' 🔮 *Projection*: {utils.get_team_name(away_abbrev)} *{utils.format_number(matchup.away_projected, decimal_places=2)}*-*{
                utils.format_number(matchup.home_projected, decimal_places=2)}* {utils.get_team_name(home_abbrev)}'
        ]
        schedule.append({
            'type': 'context',
            'elements': [utils.get_mrkdwn_text('\n'.join(breakdown_text))]
        })

    return schedule


def get_record(team):
    return f'({team.wins}-{team.losses})'

# const TEAM_1 = TEAMS["HM"];
# const TEAM_2 = TEAMS["TIDE"];

# let team1Wins = 0;
# let team2Wins = 0;
# let streak;
# let last;

# for (const matchup of MATCHUPS) {
#   const { winner, loser } = matchup;
#   const matchupTeams = [TEAM_1, TEAM_2];
#   if (!matchupTeams.includes(winner) || !matchupTeams.includes(loser)) {
#     continue;
#   }

#   if (winner === TEAM_1) {
#     team1Wins++;
#   } else {
#     team2Wins++;
#   }

#   if (!streak || streak[0] !== winner) {
#     streak = [winner, 1];
#   } else {
#     streak[1]++;
#   }

#   last = matchup;
# }

# let summary = "*H2H*: ";
# if (team1Wins > team2Wins) {
#   summary += `_${TEAM_1}_ leads *${team1Wins}-${team2Wins}*`;
# } else if (team2Wins > team1Wins) {
#   summary += `_${TEAM_2}_ leads *${team2Wins}-${team1Wins}*`;
# } else {
#   summary += `tied *${team1Wins}-${team2Wins}*`;
# }
# console.log(summary);

# console.log(`*Streak*: _${streak[0]}_ - *W${streak[1]}*`);

# const { year, week, winner, loser, winnerScore, loserScore } = last;
# const isWeek = !isNaN(parseInt(week));
# console.log(
#   `*Last*: ${year} ${
#     isWeek ? "Week " : ""
#   }${week} - _${winner}_ *${winnerScore}-${loserScore}* _${loser}_`
# );
