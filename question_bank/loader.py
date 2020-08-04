import logging
import sys
import os
import csv
from card import Card
sys.path.append(r"../gameplay")
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.CRITICAL)
logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)

class QuestionLoader:
    
    def __init__(self, path_to_question_files: str, type: str):
        LOG.info("Call to QuestionLoader.__init__")
        self.type = type
        self.question_file_path = path_to_question_files
        self.question_collection = self._load_questions()
        
    def _load_questions(self):
        LOG.info("Call to QuestionLoader._load_questions")
        LOG.info("Loading questions from {}".format(self.question_file_path))

        questions = []

        with open(os.path.join(self.question_file_path, "questions.txt")) as file:
            question_reader = csv.reader(file, delimiter='\t')
            for thisLine in question_reader:
                if thisLine[0] == self.type:
                    questions.append(Card(thisLine[0], thisLine[1], thisLine[2], thisLine[5]))
                    #print(thisLine)
        return questions

