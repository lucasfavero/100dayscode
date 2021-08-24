import random


def convert_choice_name(choice):
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"
    return choice_name


def print_choices(human, machine):
    print(f"Human choice: {convert_choice_name(human)}, Machine choice: {convert_choice_name(machine)} ")


while True:
    machine_choice = random.choice([1, 2, 3])
    human_choice = int(input("What do you want? Type 1 for Rock, 2 for Paper, 3 for Scissors: "))

    if (human_choice < 1) or (human_choice > 3):
        print("Invalid choice, choose again.")
        continue

    if machine_choice == human_choice:
        print_choices(human_choice, machine_choice)
        print("We have a draw!")
    elif (machine_choice == 1) and (human_choice == 3):
        print_choices(human_choice, machine_choice)
        print("The machine own!")
    elif (machine_choice == 2) and (human_choice == 1):
        print_choices(human_choice, machine_choice)
        print("The machine own!")
    elif (machine_choice == 3) and (human_choice == 2):
        print_choices(human_choice, machine_choice)
        print("The machine own!")
    else:
        print_choices(human_choice, machine_choice)
        print("The human own!")
