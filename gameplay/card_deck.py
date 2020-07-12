from card import Card
import logging
import sys
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class CardDecks:
    
    def __init__(self):
        LOG.info("Call to CardDecks")
        self.red_deck = CardDeck()
        self.white_deck = CardDeck()
        self.blue_deck = CardDeck()
        self.green_deck = CardDeck()
            
class CardDeck:
    
    def __init__(self):
        LOG.info("Call to CardDeck")
        self.cards = []
        for question in range(25):
            self.cards.append(Card())
            
    def load_questions_from_file(self, path: str):
        pass
            
    def load_questions_from_file(self, path: str):
        pass