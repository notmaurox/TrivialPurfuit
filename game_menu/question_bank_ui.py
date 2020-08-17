import logging
import sys

from writer import QuestionWriter
from loader import QuestionLoader

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# TODO? Add descrete class for question

class QuestionBankInterface:
    
    def __init__(self):
        self.PATH_TO_QUESTIONS = "path/to/questions/within/repo"
        LOG.info("QuestionBankInterface constructor")
        self.loader = QuestionLoader(self.PATH_TO_QUESTIONS)
        self.question_writer = QuestionWriter(
            self.PATH_TO_QUESTIONS,
            self.loader.question_collection
        )
        
    def add_question(self, q_type, q, a):
        LOG.info("Call to QuestionBankInterface.add_question")
        self.question_writer.insert_question(q_type, q, a)
        
    def save_questions(self):
        LOG.info("Call to QuestionBankInterface.save_questions")
        self.question_writer.write_questions_to_files()
        
    def view_questions(self):
        LOG.info("Call to QuestionBankInterface.view_questions")
        LOG.info("Display questions")