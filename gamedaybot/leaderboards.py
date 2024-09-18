from utils.util import create_dict

# TODO: Get teams from utils
teams = create_dict(["CL", "FIG", "GOGA", "HM", "KTT", "LNU" "RR", "TIDE", "WFH", "YEAH"],
                    {"TD": 0, "QB": 0, "RB": 0, "WR": 0, "TE": 0, "D/ST": 0, "K": 0})


def get(league):
    for i in range(1, league.current_week - 1):
        box_scores = league.box_scores(i)
