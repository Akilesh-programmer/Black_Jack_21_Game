# Importing random module
import random


# Putting the entire game into a function for performing recursion.
def game():
    # Creating a cards list
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Creating some storages needed to run the game.
    computer_cards = []
    player_cards = []
    computer_total = 0
    player_total = 0

    # Creating two random cards for computer and adding it to the computer_cards list.
    for n in range(0, 2):
        random_card = random.randint(1, 13)
        computer_cards.append(cards[random_card - 1])
    # Creating two random cards for player and adding it to the player_cards list.
    for n in range(0, 2):
        random_card = random.randint(1, 13)
        player_cards.append(cards[random_card - 1])

    # Getting the total of the computer's cards.
    for card in computer_cards:
        computer_total += card
    # Getting the total of the player's cards.
    for card in player_cards:
        player_total += card

    # Checking if anyone got 21 as the total. If so ending the game.
    if computer_total == 21:
        print("You lose. Computer wins.")
    if player_total == 21:
        print("You win. Computer lose.")

    # Ace can be used as both 1 and 11. So if anyone got ace and their total exceeded 21 we are making that ace count
    # as 1.
    if 11 in computer_cards:
        if computer_total > 21:
            computer_total -= 10

    if 11 in player_cards:
        if player_total > 21:
            player_total -= 10

    # Showing the first card of the computer to the player
    first_card_of_computer = computer_cards[0]
    print(f"This is the first card of the computer: {first_card_of_computer}")

    # Creating a boolean variable to end the game.
    game_ends = False

    # Creating a variable to count the number of times a while loop is running.
    times_running = 0

    # Showing the user his cards and his total.
    print(f"Your cards are{player_cards} and your score is {player_total}")

    # When game is not ended and when the user wants to draw another card doing the following.
    while game_ends == False and input("Type 'y' to draw another card else type 'n'.") == "y":
        # First adding 1 to times_running to track the number of times this loop is running.
        times_running += 1
        # If this loop is running for the second time or more again showing the user his cards and his total.
        if times_running > 1:
            print(f"Your cards are{player_cards} and your score is {player_total}")
        # Generating a random card.
        random_card = random.randint(1, 13)
        # Adding the new card to player_cards list.
        player_cards.append(cards[random_card - 1])

        # Adding the new one to the total also.
        player_total += cards[random_card - 1]
        # Again showing the user his cards and his total
        print(f"Your cards are {player_cards} and your total is {player_total}")

        # If the player's total exceeded 21 then ending the game by ending the while loop.
        if player_total > 21:
            game_ends = True
            print("You lose your total exceeded 21.")

    if not game_ends:
        # If the game is not ended then making the computer to draw cards until it's total is less than 16.
        while computer_total < 16:
            # Generating the random card.
            random_card = random.randint(1, 13)
            # Adding the new card to the computer_cards list.
            computer_cards.append(cards[random_card - 1])
            # Adding the new card to the total
            computer_total += cards[random_card - 1]

    if not game_ends:
        # If the game is not ended then now computing the winner by looking into the conditions of the game itself.
        if computer_total > 21:
            print("You win")
        elif player_total > computer_total:
            print("You win")
        elif computer_total > player_total:
            print("You lose")
        elif computer_total == player_total:
            print("Draw.")

        # Finally showing the cards and totals of both player and the computer.
        print(f"Computer cards are {computer_cards} and total is {computer_total}")
        print(f"Your cards are {player_cards} and your total is {player_total}")

    # Restarting the game if the user wants to.
    if input("Type 'y' to restart the game and type 'n' to exit the game.") == "y":
        game()
    else:
        print("Thanks for playing")


# Starting the game.
game()
