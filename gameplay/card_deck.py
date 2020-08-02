from card import Card
import logging
import sys
sys.path.append("../question_bank")
from loader import QuestionLoader
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
import random

## This should be adapted to remove CardDecks and instead have all categories in CardDeck.  Instantiation will change a little bit


class CardDecks:
    
    def __init__(self):
        LOG.info("Call to CardDecks.__init__")
        self.red_deck = CardDeck("Events")              # Are these the right color to category mappings?  If we want to stick with colors, that's fine
        self.white_deck = CardDeck("Independence Day")
        self.blue_deck = CardDeck("People")
        self.green_deck = CardDeck("Places")
        
    def get_green_card(self):
        return self.green_deck.deal_card()
        
    def get_white_card(self):
        return self.white_deck.deal_card()
        
    def get_blue_card(self):
        return self.blue_deck.deal_card()
        
    def get_red_card(self):
        return self.red_deck.deal_card()

    def draw_card_by_type(self, type):  # Move this logic to game board
        if type == "red":
            return self.get_red_card()
        if type == "white":
            return self.get_white_card()
        if type == "blue":
            return self.get_blue_card()
        if type == "green":
            return self.get_green_card()
            
class CardDeck:
    
    def __init__(self, type):
        LOG.info("Call to CardDeck.__init__")
        path = r"../question_bank/"
        self.cards = []
        self.type = type
        self.load_questions_from_file(path, type)

    def load_questions_from_file(self, path: str, type):
        LOG.info("Call to CardDeck.load_questions_from_file")
        self.cards = QuestionLoader(path, type).question_collection
        print("Sample card question", self.cards[0].question)
        print("Sample card answer", self.cards[0].answer)

    def deal_card(self):
        n = len(self.cards)-1
        i = random.randint(0,n)
        card = self.cards.pop(i)
        return card

