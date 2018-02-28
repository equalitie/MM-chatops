import local_settings as conf

from github import Github
from mattermostdriver import Driver
from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to


@respond_to('who bad?')
def gh_bad(message):
    g = Github(conf.GH_access_token)
    my_organizations = {organization.name: organization for organization in g.get_user().get_orgs()}
    org = my_organizations[conf.GH_ORG]
    org_members_no_2fa = [member.login for member in org.get_members(filter_="2fa_disabled")]

    msg = '\n' + '\n'.join('- ' + (x) for x in (org_members_no_2fa))
    message.reply('%s' % (msg))

gh_bad.__doc__ = "find GH org accnts w/o 2fa enabled"
