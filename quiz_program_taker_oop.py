#Import Library of Choice
import random

#Read questions from the saved file
def load_questions_from_file(filename="quiz_questions.txt"):
    questions = []
    try:
        with open(filename, "r") as file:
            content = file.read().strip().split("---n")
            for block in content:
                lines = block.strip().split("\n")
                if len(lines)>= 6:
                    question_text = lines[0].replace("Question: ", "")
                    choices = {
                        'a': lines [1][3:].strip(),
                        'b': lines [2][3:].strip(),
                        'c': lines [3][3:].strip(),
                        'd': lines [4][3:].strip()
                    }
                    correct_choice = lines[5].replace("Correct Answer is: ", "").strip()
                    questions.append({
                        "question": question_text,
                        "options": choices,
                        "answer": correct_choice
                    })
        return questions
    except FileNotFoundError:
        print("No quiz questions found. Make sure to run the quz_maker_game before running the program.")    
        return []
#Ask a question to the user and check the answer
def ask_question(question_data):
    print("\n" + question_data["question"])
    for key, option in question_data["options"].items():
        print(f"{key}) {option}")

    user_answer = input("Your answer (a/b/c/d): ").lower()
    while user_answer not in ['a', 'b', 'c', 'd']:
        user_answer = input("Invalid answer. Please enter within the choices a/b/c/d: ").lower()

    if user_answer == question_data["answer"]:
        print("Your answer is Correct!!")
        return True
    else:
        correct_option = question_data["options"][question_data["answer"]]
        print(f"Your answer is Wrong! The correct answer is: {question_data['answer']}){correct_option}")
        return False 
    
#Run the quiz game
def run_quiz():
    print("Welcome to the quiz game!")
    saved_questions = load_questions_from_file()

    if not saved_questions:
        return

    random.shuffle(saved_questions)
    score = 0

    for question in saved_questions:
        if ask_question(question):
            score += 1

    print(f"\nQuiz has been completed! Your score is {score} out of {len(saved_questions)}.")

run_quiz()