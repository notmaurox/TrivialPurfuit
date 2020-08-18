import logging
import sys
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.CRITICAL)
logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)

class Card:
    
    def __init__(self, type, question, answer):
        LOG.info("Call to Card.__init__")
        self.type = type
        self.question = question
        self.answer = answer
        #self.difficulty = difficulty

    def print(self):
        print("Type:", self.type)
        print("Question:", self.question)
        print("Answer:", self.answer)
        print("Difficulty:", self.difficulty)
