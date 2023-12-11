from data import question_data


class Quiz:
    def is_answer_right(self, user_input, answer):
        if user_input == answer:
            print(f"Correct!")
            # Checking if user was correct and increasing score
            return True
        else:
            print(f"Wrong!")
            return False

    def calculate_score(self, score):
        print(f"Game over\nYou had {score} correct guesses!")
