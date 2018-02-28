# Basic configuration mostly ripped from the docs
from local_settings import BOT_URL, BOT_LOGIN, BOT_PASSWORD, BOT_TEAM

SSL_VERIFY = True
DEBUG = True

PLUGINS = [
    'mattermost_bot.plugins',
    'plugins',
]

# Docs + regexp or docs string only
PLUGINS_ONLY_DOC_STRING = False

# Ignore broadcast message
IGNORE_NOTIFIES = ['@channel', '@all', '@here']

# Threads num
WORKERS_NUM = 10

'''
# Custom default reply module

Example:
filename:
    my_default_reply.py
code:
    def default_reply(dispatcher, raw_msg):
        dispatcher._client.channel_msg(
            raw_msg['channel_id'], dispatcher.get_message(raw_msg)
        )
settings:
    DEFAULT_REPLY_MODULE = 'my_default_reply'
'''
DEFAULT_REPLY_MODULE = None

# or simple string for default answer
# DEFAULT_REPLY = "pants pants pants"

'''
If you use Mattermost Web API to send messages (with send_webapi()
or reply_webapi()), you can customize the bot logo by providing Icon or Emoji.
If you use Mattermost API to send messages (with send() or reply()),
the used icon comes from bot settings and Icon or Emoji has no effect.
'''
BOT_ICON = 'http://lorempixel.com/64/64/abstract/7/'
BOT_EMOJI = ':godmode:'
