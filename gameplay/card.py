import logging
import sys
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class Card:
    
    def __init__(self, type, qestion, answer):
        LOG.info("Call to Card.__init__")
        self.type = "TYPE"
        self.question = "QUESITON"
        self.answer = "ANSWER"
