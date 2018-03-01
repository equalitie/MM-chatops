import pprint


def default_reply(dispatcher, raw_msg):
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(raw_msg)
