import local_settings as conf
import pprint

from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to


@listen_to('\W?\#(\d+)\#?(\d+)?\W?')
def redmine_issue_responder(message, number, foo):
    pp = pprint.PrettyPrinter(indent=4)
    msg = ' https://redmine.equalit.ie/issues/' + number
    message.reply(msg)
    pp.pprint("XXX: " + number + " foo: " + str(foo) + " string: " + message.get_message())
