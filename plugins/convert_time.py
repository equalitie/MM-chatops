import os
import local_settings as conf

from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to

from datetime import datetime
import pytz
from mattermostdriver import Driver

time_fmt = "%A %H:%M:%S %z"
regex = r'^localtime @(.*)'

mm = Driver({'url': conf.MM_HOST,
             'token': conf.MM_TOKEN,
             'scheme': conf.MM_SCHEME,
             'port': conf.MM_PORT,
             'basepath': '/api/v4',
             'verify': True})
mm.login()


@listen_to(regex)
def convert_time(message, username):

    mm_users = mm.users.get_users()
    user = [user for user in mm_users if user['username'] == username]
    if len(user) == 0:
        message.reply("%s user not found" % (r.group(1)))
        return False
    elif len(user) == 1:
        tz = user[0]['position']
        if tz not in pytz.all_timezones:
            message.reply("tz: '%s' not found in pytz.all_timezones" % (tz))
        else:
            date = datetime.now(pytz.timezone(tz)).strftime(time_fmt)
            message.reply("it's now %s for @%s" % (date, username))
        return True
    else:
        message.reply("ask me something sensible")

convert_time.__doc__ = "localtime for a user"
