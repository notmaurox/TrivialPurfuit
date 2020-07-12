import logging
import sys

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
        return []