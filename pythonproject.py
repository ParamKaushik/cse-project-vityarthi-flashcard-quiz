import time
import random

# Flashcards (manual options)
flashcards = {
    "What is the capital of France?": {
        "answer": "Paris",
        "options": ["London", "Paris", "Berlin", "Rome"]
    },
    "What is 5 + 7?": {
        "answer": "12",
        "options": ["10", "11", "12", "13"]
    },
    "What is the chemical symbol for water?": {
        "answer": "H2O",
        "options": ["CO2", "O2", "H2O", "NaCl"]
    }
}

FAST_THRESHOLD = 3
FAST_BONUS = 1

# Input validation
def get_valid_input(prompt, valid=None):
    while True:
        ans = input(prompt).strip()

        if ans.lower() == "quit":
            return "quit"

        if valid is None or ans.lower() in valid:
            return ans.lower()

        print("Invalid input, try again.")

# Add a flashcard
def add_flashcard():
    print("\n--- Add Flashcard ---")
    
    question =input("Question: ").strip()
    if question.lower() == "quit":
        return

    answer=input("Correct answer: ").strip()
    if answer.lower() == "quit":
        return

    print("Enter FOUR options (including the correct one).")
    options = []
    for i in range(4):
        opt = input(f"Option {i+1}: ").strip()
        if opt.lower() == "quit":
            return
        options.append(opt)

    flashcards[question] = {"answer": answer, "options": options}
    print("Flashcard added!\n")

# View flashcards
def view_flashcards():
    print("\n--- Flashcards ---")
    for i, (q, data) in enumerate(flashcards.items(), start=1):
        print(f"{i}. {q}  →  {data['answer']}")
    print()

# Ask a single question
def ask_question(question, data):
    print("\nQuestion:", question)
    opts = data["options"]

    for i, opt in enumerate(opts):
        print(f"{i+1}. {opt}")

    start = time.time()
    ans = get_valid_input("Your answer (1-4): ", valid=["1", "2", "3", "4"])
    end = time.time()

    if ans == "quit":
        return "quit", 0

    chosen = opts[int(ans) - 1]
    correct = data["answer"]

    if chosen.lower() == correct.lower():
        print("Correct!")
        points = 1

        if end - start <= FAST_THRESHOLD:
            points += FAST_BONUS
            print("Fast answer bonus!")

        return True, points
    else:
        print("Wrong!")
        print("Correct answer:", correct)
        return False, 0


# Run quiz
def start_quiz():
    score = 0
    total = 0

    questions = list(flashcards.items())
    random.shuffle(questions)

    print("\nStarting quiz (type 'quit' anytime)\n")

    for q, data in questions:
        result, pts = ask_question(q, data)

        if result == "quit":
            break

        total += 1
        score += pts

    print("\nQuiz finished!")
    print(f"Score: {score}/{total}")
    print()

# Main menu
def main():
    while True:
        print("1. Start Quiz")
        print("2. Add Flashcard")
        print("3. View Flashcards")
        print("4. Quit")

        choice =get_valid_input("Choose: ", valid=["1", "2", "3", "4"])
        if choice == "1":
            start_quiz()
        elif choice== "2":
            add_flashcard()
        elif choice== "3":
            view_flashcards()
        elif choice== "4":
            print("Bye!")
            break


if __name__ =="__main__":
    main()
