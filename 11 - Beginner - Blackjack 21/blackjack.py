import random

keep_playing = True

while keep_playing:
    cards = [11, 2, 3, 4, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = random.choices(cards, k=2)
    computer_cards = random.choices(cards, k=2)

    print(f"Player hand: {player_cards}")
    print(f"Computer hand: [{computer_cards[0]}] + X")

    another_card = input("Do you want another card? Type 'y' or 'n': ")

    while another_card == 'y':
        player_cards += random.choices(cards, k=1)
        if sum(player_cards) > 21:
            break

        if sum(computer_cards) < 17:
            computer_cards += random.choices(cards, k=1)

        print(f"Player hand: {player_cards} -> {sum(player_cards)}")
        print(f"Computer hand: {computer_cards[:-1]} + X -> {sum(computer_cards[:-1])}")

        another_card = input("Do you want another card? Type 'y' or 'n': ")

    if 21 >= sum(player_cards) > sum(computer_cards):
        print(f"Computer hand: {computer_cards} -> {sum(computer_cards)}")
        print(f"You won! {player_cards} -> {sum(player_cards)} ")
    elif sum(player_cards) == sum(computer_cards):
        print(f"Computer hand: {computer_cards} -> {sum(computer_cards)}")
        print(f"Player hand: {player_cards} -> {sum(player_cards)} ")
        print(f"Draw!")
    else:
        print(f"Player hand: {player_cards} -> {sum(player_cards)} ")
        print(f"Computer won! {computer_cards} -> {sum(computer_cards)} ")

    play_again = input(f"Do you want play again? Type 'y' or 'n': ")

    if play_again == 'n':
        keep_playing = False
