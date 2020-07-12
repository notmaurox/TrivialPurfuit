from dice import Die
from players import Player
from card_deck import CardDeck
from typing import List

class GameBoard:
    
    def __init__(self, num_players: int, player_names: List[str]):
        self.players = []
        self.card_deck = CardDeck()
        self.die = Die(num_sides=6)
        
        for player_num in range(0, num_players):
            self.players.append(Player(name=player_names[player_num]))
            
        