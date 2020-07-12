from dice import Die
from player import Player
from card_deck import CardDeck
from typing import List
from game_position import GamePositions

class GameBoard:
    
    def __init__(self, num_players: int, player_names: List[str]):
        self.players = []
        self.card_decks = CardDecks()
        self.die = Die(num_sides=6)
        
        for player_num in range(0, num_players):
            self.players.append(Player(name=player_names[player_num]))
            
        self.game_positions = GamePositions()
            
        