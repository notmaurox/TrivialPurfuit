import logging
import sys
import os
import csv

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

        with open(os.path.join(path_to_question_files, "questions.txt")) as questions:
            question_reader = csv.reader(questions, delimiter='\t')
            for thisLine in question_reader:
                questions.append(Question(thisLine[0], thisLine[1], thisLine[2]))

        return questions

class Question:
    def __init__(self, category, question, difficulty):
        self.category = ""
        self.question = ""
        self.difficulty = None
