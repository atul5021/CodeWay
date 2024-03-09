import random

def load_questions():
    questions = [
        {"question": "What is the capital of India?",
         "choices": ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
         "correct_answer": 0},
        
        {"question": "Who is known as the 'Master Blaster' in Indian cricket?",
         "choices": ["Sachin Tendulkar", "Virat Kohli", "Rahul Dravid", "Virender Sehwag"],
         "correct_answer": 0},
              
        {"question": "Who is the current Prime Minister of India?",
         "choices": ["Narendra Modi", "Manmohan Singh", "Rahul Gandhi", "Amit Shah"],
         "correct_answer": 0},
        
        {"question": "Which Indian festival is known as the Festival of Lights?",
         "choices": ["Holi", "Diwali", "Navratri", "Eid"],
         "correct_answer": 1},
        
    ]
    return questions

def display_rules():
    print("Welcome to the Quiz Game!")
    print("Rules:")
    print("- You will be asked multiple-choice questions.")
    print("- Choose the correct answer from the provided options.")
    print("- Each correct answer earns you a point.")
    print("- At the end, your final score will be displayed.")
    print("Let's get started!\n")

def present_question(question):
    print(question["question"])
    for index, choice in enumerate(question["choices"], start=1):
        print(f"{index}. {choice}")
    user_answer = input("Your answer (enter the number): ")
    return int(user_answer)

def evaluate_answer(user_answer, correct_answer):
    return user_answer == correct_answer + 1  

def quiz_game():
    questions = load_questions()
    score = 0

    display_rules()

    for question in questions:
        user_answer = present_question(question)
        if evaluate_answer(user_answer, question["correct_answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['correct_answer'] + 1}: {question['choices'][question['correct_answer']]}\n")

    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    while True:
        quiz_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye.")
            break
