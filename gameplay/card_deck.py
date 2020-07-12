from card import Card

class CardDecks:
    
    def __init__(self):
        self.red_deck = CardDeck()
        self.white_deck = CardDeck()
        self.blue_deck = CardDeck()
        self.green_deck = CardDeck()
            
class CardDeck:
    
    def __init__(self):
        self.cards = []
        for question in range(25):
            self.cards.append(Card())
            
    def load_questions_from_file(self, path: str):
        pass
            
    def load_questions_from_file(self, path: str):
        pass