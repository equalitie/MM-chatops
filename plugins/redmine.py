import local_settings as conf

from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to


@listen_to('\W#(\d+)\W')
def redmine_issue_responder(message, number):
    msg = ' https://redmine.equalit.ie/issues/' + number
    message.reply(msg)
