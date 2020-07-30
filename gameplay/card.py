import logging
import sys
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class Card:
    
    def __init__(self, type, question, answer):
        LOG.info("Call to Card.__init__")
        self.type = "TYPE"
        self.question = question
        self.answer = answer
