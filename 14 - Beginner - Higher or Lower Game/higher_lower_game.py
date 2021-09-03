import random
from art import logo, vs
from game_data import data


def rand_data(game_data):
    entity = random.choice(game_data)
    entity = entity.values()
    return list(entity)


def winner(entity_1, entity_2):
    if entity_1[1] > entity_2[1]:
        return 'a'
    elif entity_1[1] < entity_2[1]:
        return 'b'
    else:
        return 'draw'


def print_entity(entity_1, entity_2):
    return print(f"{entity_1[0]}, {entity_1[1]} millions vs {entity_2[0]}, {entity_2[1]} millions.")


def game():
    print(logo)
    score = 0
    keep_playing = True

    while keep_playing:

        print(f"You score is: {score}. ")

        if score == 0:
            entity_1 = rand_data(data)
        elif result == 'b':
            entity_1 = entity_2

        print(f"Compare A: {entity_1[0]}, {entity_1[2]}, from {entity_1[3]}. ")
        print(vs)
        entity_2 = rand_data(data)
        print(f"Compare B: {entity_2[0]}, {entity_2[2]}, from {entity_2[3]}. ")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        result = winner(entity_1, entity_2)

        if choice == result:
            score += 1
            print_entity(entity_1, entity_2)
            print("You're right!")
        elif choice == 'draw':
            print_entity(entity_1, entity_2)
            print("Draw")
        else:
            print_entity(entity_1, entity_2)
            print("You're wrong!")
            keep_playing = False


play_again = True
while play_again:
    game()
    play_game = input("Do you want to play again?: Type 'y' or 'n': ").lower()

    if play_game == 'n':
        play_again = False

