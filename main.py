from espn_api.football import League
from gamedaybot.chat.slack import Slack

import datetime
import json
import os
import pytz
import messages.leaderboards as leaderboards
import messages.recap as recap
import messages.schedule as schedule
import messages.scoreboard as scoreboard

def main():
    espn_s2 = os.getenv('ESPN_S2')
    league_id = os.getenv('LEAGUE_ID')
    slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')
    swid = os.getenv('SWID')
    year = int(os.getenv('LEAGUE_YEAR'))

    league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)

    now = datetime.datetime.now(pytz.timezone('America/Los_Angeles'))
    weekday = now.strftime('%a')
    blocks = []
    if weekday == 'Tue':
        if now.hour < 12:
            blocks = recap.get(league)
        else:
            blocks = leaderboards.get(league)
    elif weekday == 'Thu':
        blocks = schedule.get(league)
    else:
        blocks = scoreboard.get(league)

    slack_bot = Slack(slack_webhook_url)
    slack_bot.send_message(blocks)

if __name__ == '__main__':
    main()
