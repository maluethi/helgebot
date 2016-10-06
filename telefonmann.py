import sopel.module
from pylms.server import Server
import json

config_file = "helge_config.json"

with open(config_file, 'r') as f:
    config = json.load(f)

try:
    sc = Server(hostname=config["server"], port=9090)
    print sc.get_version()
    sc.connect()
    sq = sc.get_player(config["player"])
except:
    sq = None
    #raise EnvironmentError("Cannot connect logitech to server.")




def play_song(title):
    songs = {'telefonmann': '1',
             'break':       '2',
             'goldman':     '3'}

    if title not in songs:
        return 'I don\'t know this song'

    if sq is None:
        return ''

    sq.request("favorites playlist play item_id:2." + songs[title] + "\n")  # "1\n" )
    return None


@sopel.module.rule(ur'(?i)\b^(hey)\,?\s+\1\b')
def telefonmann(bot, trigger):
    bot.say('Telefonmann!')
    bot.say(play_song('telefonmann'))

@sopel.module.rule(ur'(?i)(brake together)\b')
def brake(bot, trigger):
    bot.say("zusammen")
    bot.say(play_song('break'))

@sopel.module.rule(ur'(?i)(break)\b')
def breake(bot, trigger):
    bot.say('I never break...')

@sopel.module.rule(ur'(?i)(gold man)\b | (goldman)\b/gmi')
def goldman(bot, trigger):
    bot.say('DAMIAN!!!!')
    bot.say(play_song('goldman'))

@sopel.module.rule(ur'(?i)(gold man)\b | (goldman)\b/gmi')
def play_a_song(bot, trigger):
    bot.say('ladidadida, just for' + trigger.nick)
