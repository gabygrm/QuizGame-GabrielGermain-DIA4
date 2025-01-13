import time

def intro():
    print("Welcome to the General Culture Quiz!")
    print("You will answer 10 questions, each with 4 possible answers.")
    print("Type the number corresponding to your choice and press Enter.")
    print("Let's see how much you know!")
    time.sleep(2)

def outro(score, total):
    print("\nQuiz Complete!")
    print(f"You scored {score}/{total}.")
    if score == total:
        print("Excellent! You're a genius!")
    elif score > total // 2:
        print("Good job! You know quite a bit.")
    else:
        print("Keep learning! Knowledge is power.")

def ask_question(question, options, correct_answer):
    print(f"\n{question}")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            answer = int(input("Your answer: "))
            if 1 <= answer <= 4:
                return answer == correct_answer
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def main():
    intro()

    questions = [
        ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3),
        ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "J.K. Rowling", "Mark Twain", "Jane Austen"], 1),
        ("What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars", "Saturn"], 2),
        ("Which element has the chemical symbol 'O'?", ["Oxygen", "Gold", "Osmium", "Silver"], 1),
        ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], 3),
        ("What is the smallest prime number?", ["1", "2", "3", "5"], 2),
        ("Which ocean is the largest?", ["Atlantic", "Indian", "Arctic", "Pacific"], 4),
        ("What year did the Titanic sink?", ["1912", "1905", "1920", "1898"], 1),
        ("Who discovered penicillin?", ["Alexander Fleming", "Marie Curie", "Isaac Newton", "Louis Pasteur"], 1),
        ("What is the square root of 64?", ["6", "7", "8", "9"], 3)
    ]

    score = 0
    total = len(questions)

    for question, options, correct_answer in questions:
        if ask_question(question, options, correct_answer):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    outro(score, total)

if __name__ == "__main__":
    main()
