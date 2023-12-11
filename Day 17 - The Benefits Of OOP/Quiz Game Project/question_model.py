from data import question_data
import random


class Question:
    def __init__(self):
        self.questions = question_data
        # Importing questions as a Question class attribute

    def choose_question(self):
        """
        This method chooses a random question from the questions attribute, removes it from the list and returns the question
        :return:
        """
        new_question = self.questions[random.randint(0, len(self.questions) - 1)]
        self.questions.remove(new_question)
        text = new_question["question"]
        answer = new_question["correct_answer"]
        return text, answer

    def is_last_question(self):
        if len(self.questions) == 0:
            return True
        else:
            return False