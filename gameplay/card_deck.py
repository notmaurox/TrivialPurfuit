from card import Card
import logging
import sys
sys.path.append("../question_bank")
from loader import QuestionLoader
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class CardDecks:
    
    def __init__(self):
        LOG.info("Call to CardDecks.__init__")
        self.red_deck = CardDeck()
        self.white_deck = CardDeck()
        self.blue_deck = CardDeck()
        self.green_deck = CardDeck()
        
    def get_green_card(self):
        pass
        
    def get_white_card(self):
        pass
        
    def get_blue_card(self):
        pass
        
    def get_white_card(self):
        pass
            
class CardDeck:
    
    def __init__(self, type):
        LOG.info("Call to CardDeck.__init__")
        path = r"../question_bank/"
        self.cards = []
        self.type = type
        self.load_questions_from_file(path)

            
    def load_questions_from_file(self, path: str):
        LOG.info("Call to CardDeck.load_questions_from_file")
        self.cards = QuestionLoader(path).question_collection
        print("Sample card question", self.cards[0].question)
        print("Sample card answer", self.cards[0].answer)

    def deal_card():
        pass
