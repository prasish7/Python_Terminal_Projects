import random

questions = {
    "What is the capital of France?": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome", ],
    "What is 2 + 2?": ["A) 3", "B) 4", "C) 5", "D) 6", ],
    "What is the largest planet in our solar system?": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars", ],
    "Who wrote 'Hamlet'?": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen", ],
    "What is the boiling point of water?": ["A) 90°C", "B) 100°C", "C) 110°C", "D) 120°C", ],
}
answers = {
    "What is the capital of France?": "C",
    "What is 2 + 2?": "B",
    "What is the largest planet in our solar system?": "B",
    "Who wrote 'Hamlet'?": "C",
    "What is the boiling point of water?": "B",
}
score = 0
total_questions = len(questions)

for question, options in questions.items():
    print("\n" + question)
    for option in options:
        print(option)
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    
    if user_answer == answers[question]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answers[question]}.")
print(f"\nYour final score is {score} out of {total_questions}.")