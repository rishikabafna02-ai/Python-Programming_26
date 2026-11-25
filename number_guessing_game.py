
# ---------------------------------------------------
#  NUMBER GUESSING GAME
#  A fun beginner python project
# ---------------------------------------------------

import random

print("=====================================")
print("   WELCOME TO THE NUMBER GUESSING GAME")
print("=====================================")

# player's score across rounds
score = 0

play_again = "yes"

while play_again == "yes":

    # let player pick difficulty
    print("\nChoose difficulty level:")
    print("1. Easy   (1 to 50,  10 chances)")
    print("2. Medium (1 to 100, 7 chances)")
    print("3. Hard   (1 to 200, 5 chances)")

    level = input("Enter choice (1/2/3): ")

    if level == "1":
        lower = 1
        upper = 50
        chances = 10
    elif level == "2":
        lower = 1
        upper = 100
        chances = 7
    elif level == "3":
        lower = 1
        upper = 200
        chances = 5
    else:
        print("Invalid choice, setting to Medium by default.")
        lower = 1
        upper = 100
        chances = 7

    # computer picks a random number
    secret_number = random.randint(lower, upper)

    print("\nI have picked a number between", lower, "and", upper)
    print("You have", chances, "chances to guess it. Good luck!")

    attempts = 0
    guessed_correctly = False

    while attempts < chances:
        guess = input("\nEnter your guess: ")

        # check if input is a proper number
        if guess.isdigit() == False:
            print("That's not a valid number! Try again.")
            continue

        guess = int(guess)
        attempts = attempts + 1

        if guess < lower or guess > upper:
            print("Please guess within the given range!")

        elif guess < secret_number:
            print("Too low! Try a bigger number.")

            # small hint system for fun
            difference = secret_number - guess
            if difference > 20:
                print("(Hint: You are very far away)")
            elif difference <= 20 and difference > 5:
                print("(Hint: Getting closer...)")
            else:
                print("(Hint: Very close now!)")

        elif guess > secret_number:
            print("Too high! Try a smaller number.")

            difference = guess - secret_number
            if difference > 20:
                print("(Hint: You are very far away)")
            elif difference <= 20 and difference > 5:
                print("(Hint: Getting closer...)")
            else:
                print("(Hint: Very close now!)")

        else:
            print("\nCongratulations! You guessed it right!")
            print("The number was", secret_number)
            print("You took", attempts, "attempt(s).")

            # give points based on how fast they guessed
            points_earned = chances - attempts + 1
            score = score + points_earned
            print("You earned", points_earned, "points!")

            guessed_correctly = True
            break

        print("Chances left:", chances - attempts)

    if guessed_correctly == False:
        print("\nOops! You ran out of chances.")
        print("The correct number was", secret_number)

    print("Your total score so far:", score)

    play_again = input("\nDo you want to play again? (yes/no): ")
    play_again = play_again.lower()

print("\nThanks for playing! Your final score is", score)
print("=====================================")
