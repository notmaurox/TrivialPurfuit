import logging
import sys
import os
import csv
from card import Card
sys.path.append(r"../gameplay")
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class QuestionLoader:
    
    def __init__(self, path_to_question_files: str):
        LOG.info("Call to QuestionLoader.__init__")
        self.question_file_path = path_to_question_files
        self.question_collection = self._load_questions(
            path_to_question_files=self.question_file_path
        )
        
    def _load_questions(self, path_to_question_files: str):
        LOG.info("Call to QuestionLoader._load_questions")
        LOG.info("Loading questions from {}".format(path_to_question_files))

        questions = []

        with open(os.path.join(path_to_question_files, "questions.txt")) as file:
            question_reader = csv.reader(file, delimiter='\t')
            for thisLine in question_reader:
                questions.append(Card(thisLine[0], thisLine[1], thisLine[2], thisLine[4]))
                print(thisLine)
        return questions

