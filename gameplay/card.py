import logging
import sys
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class Card:
    
    def __init__(self):
        LOG.info("Call to Card")
        self.type = "TYPE"
        self.question = "QUESITON"
        self.answer = "ANSWER"
