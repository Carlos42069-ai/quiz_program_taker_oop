
import random


class QuizGame: 
    def __init__(self, filename= "quiz_questions.txt"):
        self.filename = filename
        self.questions = self.load_questions_from_file()
        self.score = 0 

    def load_questions_from_file(self):
        questions = []
        try:
            with open(self.filename, "r") as file:
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

    def ask_question(self, question_data):
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
    

    def run(self):
        print("Welcome to the quiz game!")
        if not self.questions:
            return

        random.shuffle(self.questions)
        for question in self.questions:
            if self.ask_question(question):
                self.score += 1

        print(f"\nQuiz has been completed! Your score is {self.score} out of {len(self.saved_questions)}.")

quiz = QuizGame()
quiz.run() 