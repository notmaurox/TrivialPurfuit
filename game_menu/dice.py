import numpy as np
import logging
import sys
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.CRITICAL)
logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)

class Die:
    
    def __init__(self, num_sides):
        LOG.info("Call to Die.__init__")
        self.num_sides = num_sides
        self.last_roll = []

    def roll(self):
        LOG.info("Call to Die.roll")
        this_number = np.random.randint(1, self.num_sides+1)
        LOG.info("Rolling die: " + str(this_number))
        self.last_roll = this_number
        return this_number