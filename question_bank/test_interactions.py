import unittest

from question_bank_ui import QuestionBankInterface

class TestQuestionBankInteractions(unittest.TestCase):
    
    def test_question_bank_interface(self):
        print("test_question_bank_interface")
        question_bank = QuestionBankInterface()
        
    def test_add_question(self):
        print("test_add_question")
        question_bank = QuestionBankInterface()
        question_bank.add_question("TYPE", "QUESTION", "ANSWER")
        
    def test_save_questions(self):
        print("test_save_questions")
        question_bank = QuestionBankInterface()
        question_bank.add_question("TYPE", "QUESTION", "ANSWER")
        question_bank.add_question("TYPE", "QUESTION", "ANSWER")
        question_bank.save_questions()
        
    def test_question_display(self):
        print("test_question_display")
        question_bank = QuestionBankInterface()
        question_bank.view_questions()
        