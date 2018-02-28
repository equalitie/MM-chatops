#!/usr/bin/env python
#
# Testing what we want
#
# --timball@equalit.ie
# Tue Feb 27 12:12:06 EST 2018

import local_settings as conf
import argparse
import pprint

from github import Github
from mattermostdriver import Driver

parser = argparse.ArgumentParser(description='MM Test code')
parser.add_argument("-d", "--debug", action='store_true')
args = parser.parse_args()

# let's get the list of users w/ 2fa_disabled from github
g = Github(conf.GH_access_token)
my_organizations = {organization.name: organization for organization in g.get_user().get_orgs()}
org = my_organizations[conf.GH_ORG]
org_members_no_2fa = [member.login for member in org.get_members(filter_="2fa_disabled")]

msg = ''
for i in org_members_no_2fa:
    msg += '- %s\n' % (i)
if args.debug:
    print (msg)
else:
    # let's now talk to mattermost
    mm = Driver({
        'url': conf.MM_HOST,
        'token': conf.MM_TOKEN,
        'scheme': conf.MM_SCHEME,
        'port': conf.MM_PORT,
        'basepath': '/api/v4',
        'verify': True
    })
    mm.login()

    # the assumption is that there is only one "team" with 'display_name'
    # mm_teams = mm.teams.get_teams()
    # mm_team = list(filter(lambda d: d['display_name'] == conf.MM_TEAM, mm_teams))[0]

    # the assumption is that there is only one "channel" with 'name'
    # mm_channels = mm.teams.get_public_channels(team_id=mm_team['id'])
    # mm_channel = list(filter(lambda d: d['name'] == conf.MM_CHAN_NAME, mm_channels))[0]

    post = mm.posts.create_post(options={'channel_id': conf.MM_TEST_CHANNEL_ID,
                                         'message': "%s GitHub Users Without 2FA\n" % (conf.GH_ORG) + msg,
                                         })
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(post)
