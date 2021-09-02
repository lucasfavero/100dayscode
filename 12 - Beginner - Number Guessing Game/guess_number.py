import random
import art

print(art.logo)
print("Welcome to the Number Guess!")

number = random.randint(1, 101)

print("Im thinking of a number between 1 and 100.")

play_again = "y"

while play_again == "y":
    difficulty = input("Chose a difficulty: Type 'hard' or 'easy'. ")

    if difficulty == 'hard':
        attempts = 5
    else:
        attempts = 10

    difficulty_attempts = attempts

    while attempts > 0:
        print(f"You have {attempts} attempts to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You guessed the number! [{number}] in [{difficulty_attempts - attempts}] attempts")
            break
        elif guess > number:
            print("Too high. Try again.")
        else:
            print("Too slow. Try again.")
        attempts -= 1

        if attempts == 0:
            print(f"You don't have more attempts. The number was {number} ")
    play_again = input("Do you want to play again? Type: 'y' or 'n'. ")















