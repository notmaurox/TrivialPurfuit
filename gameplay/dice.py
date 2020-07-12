import numpy as np
import logging
import sys
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class Die:
    
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def roll(self):
        this_number = np.random.randint(1, self.num_sides+1)
        LOG.info("Rolling die: " + str(this_number))
        return this_number