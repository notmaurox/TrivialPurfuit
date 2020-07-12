import sys
import logging

sys.path.insert(0, "../gameplay/")
sys.path.insert(0, "../question_bank/")

from game_board import GameBoard
from question_bank_ui import QuestionBankInterface

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class GameStarter:
    
    def __init__(self):
        LOG.info("Call to GameStarter.__init__")
        
    def start_game(self, num_players, player_names):
        LOG.info("Call to GameStarter.start_game")
        GameBoard(
            num_players, player_names
        )
        
    def view_questions(self):
        LOG.info("Call to GameStarter.view_questions")
        QuestionBankInterface()