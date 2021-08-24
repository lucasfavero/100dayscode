import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

animals_file = open("all_animals.txt", "r")
animals_content = animals_file.read().splitlines()

chosen_animal = random.choice(animals_content).lower()

print(chosen_animal)

display = []
for letter in chosen_animal:
    if letter == " ":
        display += " "
    else:
        display += "_"
print("Welcome to the Animal Specialist Hangman! You only can get 6 letters wrong! ")
print(f"Your animal has {len(chosen_animal)} characters. ")
print(f"{' '.join(display)}")
print(stages[6])

keep_guess = True
chances = 6

while keep_guess:
    got_it_right = False
    guess = input("Choose a letter: ")

    for i in range(len(chosen_animal)):
        if chosen_animal[i] == guess:
            display[i] = chosen_animal[i]
            got_it_right = True

    if got_it_right:
        print("You got the letter right. ")
        print(f"{' '.join(display)}")
        print(stages[chances], "\n")
    else:
        chances -= 1
        print(f"You got the letter wrong. You have {chances} chances.  ")
        print(f"{' '.join(display)}")
        print(stages[chances], "\n")
        if chances < 1:
            keep_guess = False
            print("You lost the game!")

    if "_" not in display:
        keep_guess = False
        print("You won the game!")
