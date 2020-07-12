import mover as mvr

import logging
import sys
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class Players:
    def __init__(self):
        self.players = []
        LOG.info("Call to players")

    def add_player(self, name, mover_color, start_pos):
        LOG.info("Call to players.add_player")
        LOG.info("Adding new player named " + name + " of color " + mover_color)
        self.players.append(Player(name, mvr.mover(mover_color, start_pos)))

    def get_player_count(self):
        LOG.info("Call to players.get_player_count")
        LOG.info("There are " + str(len(self.players)) + " players.")
        return len(self.players)

class Player:
    def __init__(self, name: str, mover: mvr):
        self.name = name
        self.mover = mover

    def get_player_color(self):
        LOG.info("Call to player.get_player_color")
        LOG.info("Player color: " + self.mover.mover_color)
        return self.mover.mover_color

    def crown_winner(self):
        LOG.info("Call to player.crown_winner")
        LOG.info("Player " + self.name + " won!")