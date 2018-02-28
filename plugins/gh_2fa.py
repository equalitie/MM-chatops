import os
import local_settings as conf

from github import Github
from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to


@respond_to('who bad?')
def gh_bad(message):
    g = Github(conf.GH_access_token)
    my_organizations = {organization.name: organization for organization in g.get_user().get_orgs()}
    org = my_organizations[conf.GH_ORG]
    org_members_no_2fa = [member.login for member in org.get_members(filter_="2fa_disabled")]

    if len(org_members_no_2fa) == 0:
        msg = "All %s organization users have 2fa enabled :tada:"
    elif len(org_members_no_2fa) > 0:
        msg = '%s without 2fa are:\n' % (conf.GH_ORG) + '\n'.join('- ' + (x) for x in (org_members_no_2fa))
        msg += "Those users can enable github 2fa at https://github.com/settings/security"
    else:
        msg = "Something strange happened in %s" % (os.path.basename(__file__))
    message.reply('%s' % (msg))

gh_bad.__doc__ = "find GH org accnts w/o 2fa enabled"
