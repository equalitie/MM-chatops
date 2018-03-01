
import local_settings as conf
import re

from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to
regex = r'\#(\d+)'


@listen_to(regex)
def redmine_issue_responder(message, number):
    url = "https://redmine.equalit.ie/issues/%s"

    l = re.findall(regex, message.get_message())
    msg = '\n'.join([url % (x) for x in l])
    message.reply(msg)
