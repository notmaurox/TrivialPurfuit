import mover as mvr

class Players:
    def __init__(self):
        self.players = []

    def add_player(self, name, mover_color, start_pos):
        print("Adding new player named", name, "of color", mover_color)
        self.players.append(Player(name, mvr(mover_color, start_pos)))

    def get_player_count(self):
        print("There are", len(self.players), "players.")
        return len(self.players)

class Player:
    def __init__(self, name: str, mover: mvr):
        self.name = name
        self.mover = mover

    def get_player_color(self):
        print("Player color:", self.mover.mover_color)
        return self.mover.mover_color

    def crown_winner(self):
        print("Player", self.name, "won!")