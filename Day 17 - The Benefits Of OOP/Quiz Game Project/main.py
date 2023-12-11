from question_model import Question
from quiz_brain import Quiz

def main():
    """
    Main quiz game
    :return:
    """
    score = 0
    question = Question()
    quiz = Quiz()

    while True:
        # Main game loop

        text, answer = question.choose_question()
        # Choosing a new question using method

        is_last_question = question.is_last_question()

        if is_last_question:
            quiz.calculate_score(score)
            break
            # Checks if it is the last question in the list and breaks the loop

        choice = input(f"Is it True or False that {text}\n").title()
        # User input

        if choice == "Quit":
            quiz.calculate_score(score)
            break
            # Checks if player wants to quit

        is_correct = quiz.is_answer_right(answer=answer, user_input=choice)
        # Check if user was correct

        if is_correct:
            score += 1
            # Add to score if user correct

    choice = input("Play again?").lower()
    if choice == "yes":
        main()


main()