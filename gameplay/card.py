import logging
import sys
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class Card:
    
    def __init__(self):
        self.type = "TYPE"
        self.question = "QUESITON"
        self.answer = "ANSWER"
        
    def card_to_deck_interface(self):
        LOG.info("test")