
import random
import time

#ADDING SOME DEFAULT QUESTIONS RELATED TO THE SUBJECR
flashcards = {
    "what circuit element controls the flow of current?":"resistor",
    "In thevenins theorem, what is resistance for the final simplified circuit called?":"Thevenins Resistance",
    "What is the chemical symbol for water?":"H2O", "how many laws of thermodynamics are there":"Four"
}

print("Welcome to the Flashcard Quiz")
#NOW,THEY CAN ADD FLASHCARDS OF THEIR OWN IF THEY WANT TO.
while True:
    add = input("Would you like to add a flashcard? (yes/no): ").lower() #AVOIDS WRONG ANSWER FOR CAPATALIZATION
    if add=="yes":
        question=input("Enter the question: ")
        answer=input("Enter the answer: ")
        flashcards[question] = answer
        print("Flashcard added!\n")
    elif add =="no":
        break
    else:
        print("Please answer with 'yes' or 'no'.")

print("\nGreat! Let's start the quiz.")#/n-ADDS SPACING
print("Type 'quit' anytime to exit.")
print("-" * 40)

#SETTING UP THE QUIZ AND THE INBITIAL SCORE TO 0 WHICH WILL BE INCREMENTED WIT EVERY CORECT ANSWER
questions =list(flashcards.keys())
score=0
total_questions=0
TIME_LIMIT=10 #giving 10 seconds per question, otherwise marks dont count

while True:
    question=random.choice(questions)
    correct_answer=flashcards[question]

    print("\nQuestion:",question)

    #ADDING A 10 SEOND TIME LIMIT
    start_time = time.time()
    user_answer=input("Your answer: ")
    end_time=time.time()
    
    if user_answer.lower()=="quit":
        break

    total_questions += 1
    time_taken = end_time - start_time

    if time_taken>TIME_LIMIT:
        print(f"Too slow! You took {time_taken:.2f} seconds.")
        print("Correct answer:", correct_answer)
        continue

    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        print("Correct answer:",correct_answer)

#SHOWING THE FINAL SCORE
print("\n Quiz Complete")
print("Correct answers:",score)
print("Total questions answered:",total_questions)

if total_questions>0:
    percentage = (score / total_questions) * 100
    print(f"Score percentage: {percentage:.2f}%")
else:
    print("No questions were answered.")

print("Thanks for playing!")