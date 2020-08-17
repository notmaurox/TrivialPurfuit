import logging
import sys

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class QuestionWriter:
    
    def __init__(self, path_to_questions, question_collection):
        LOG.info("Call to QuestionWriter.__init__")
        self.path_to_files = path_to_questions
        self.question_collection = question_collection

    def insert_question(self, q_type, q, a):
        LOG.info("Call to QuestionWriter.insert_question")
        LOG.info(
            "Inserting question type: {}, question: {}, answer: {}".format(
                q_type,
                q,
                a
            )
        )
        self.question_collection.append(
            {
                "type": q_type,
                "question": q,
                "answer": a
            }
        )

    def write_questions_to_files(self):
        LOG.info("Call to QuestionWriter.write_questions_to_files")
        LOG.info("Writing {} questions to files".format(
            len(self.question_collection)
        ))
