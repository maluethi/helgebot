from pylms.server import Server
from pylms.player import Player
import json

with open(config_file, 'r') as f:
    config = json.load(f)


sc = Server(hostname=config["server"], port=9090)
sc.connect()

print "Logged in: %s" % sc.logged_in
print "Version: %s" % sc.get_version()

sq = sc.get_player(config["player"])


cmd = "favorites playlist play item_id:1."
cmd = "favorites playlist play item_id:2\n"

print sq.request("favorites playlist play item_id:2.0\n") #"1\n" )