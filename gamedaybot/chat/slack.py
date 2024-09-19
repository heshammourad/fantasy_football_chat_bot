import requests
import json
import logging

logger = logging.getLogger(__name__)


class SlackException(Exception):
    pass


class Slack:
    """
    A class used to send messages to a Slack channel through a webhook.

    Parameters
    ----------
    webhook_url : str
        The URL of the Slack webhook to send messages to.

    Attributes
    ----------
    webhook_url : str
        The URL of the Slack webhook to send messages to.

    Methods
    -------
    send_message(text: str)
        Sends a message to the Slack channel.
    """

    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def __repr__(self):
        return "Slack Webhook Url(%s)" % self.webhook_url

    def send_message(self, blocks: str):
        headers = {'content-type': 'application/json'}

        if self.webhook_url not in (1, "1", ''):
            r = requests.post(self.webhook_url,
                              data=json.dumps({'blocks': blocks}), headers=headers)

            if r.status_code != 200:
                logger.error(r.content)
                raise SlackException(r.content)

            return r
