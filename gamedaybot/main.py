from chat.slack import Slack
from espn_api.football import League

import datetime
import os
import pytz
import recap

def main():
    espn_s2 = os.getenv('ESPN_S2')
    league_id = os.getenv('LEAGUE_ID')
    slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')
    swid = os.getenv('SWID')
    year = int(os.getenv('LEAGUE_YEAR'))

    league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)

    now = datetime.datetime.now(pytz.timezone('America/Los_Angeles'))
    weekday = now.strftime('%a')
    text = ''
    if weekday == 'Tue':
        if now.hour < 24: # TODO: Update to 12
            text = recap.get(league)

    print(text)
    slack_bot = Slack(slack_webhook_url)
    slack_bot.send_message(text)

if __name__ == '__main__':
    main()
