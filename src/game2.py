# Importing the random module for generating random numbers
import random

# Function for the Guessing Game
def GuessingGame():
    # Introduction to the game
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number from 1 to 20.")

    # Generate a random number between 1 and 20
    secret_number = random.randint(1,20)
    attempts = 0
    guess = None

    # Loop until the user guesses the correct number
    while guess != secret_number:
        try:
            # Prompt the user for a guess
            guess = int(input("Take a guess: "))
            attempts += 1

            # Provide feedback on the guess
            if guess < secret_number:
                print("Your guess is too low.")

            elif guess > secret_number:
                print("Your guess is too high.")

            elif guess == secret_number:
                print("Congratulations! You guessed the number in", attempts, "attempts.")
                break

        except ValueError:
            # Handle invalid input
            print('Invalid input. Please enter a number.')

# Function for the Blackjack game
def Blackjack():
    # Introduction to the game
    print("Welcome to blackjack!")
    print("The goal of the game is to get as close to 21 as possible without going over.")
    print("You will be dealt 2 cards and you can choose to hit or stand. \nIf you go over 21, you lose. \n\nIf you get 21, you win!\n\n")

    # Deal two random cards to the player
    random_array = [random.randint(1,11) for _ in range(2)]
    print("Your cards are:", random_array[0], "and", random_array[1])
    total = sum(random_array)
    print("Your total is:", total)
    
    # Loop for the player's turn
    while True:
        # Ask the player to hit or stand
        choice2 = input("Would you like to hit or stand? (h/s): ").lower()
        i=0
        if choice2 == 'h':
            # Add a new card to the player's hand
            new_card = random.randint(1,11)
            print("Your new card is:", new_card)
            random_array.append(new_card)
            total = sum(random_array)
            print("Your new total is:", total)
            # Check if the player has busted or won
            if total > 21:
                print("You busted!")
                break
            elif total == 21:
                print("You win!")
                break
            i =+1 

        elif choice2 == 's':
            # Finalize the player's total and compare with the dealer
            total = sum(random_array)
            print("Your final total is:", total)
            if total > 21:
                print("You busted!")
                break
            elif total == 21:
                print("You win!")
                break
            elif total < 21:
                # Simulate the dealer's turn
                dealers_card = [random.randint(1,11) for _ in range(i)]
                print("Dealer's cards total:", sum(dealers_card))
                if sum(dealers_card) == 21:
                    print("Dealer wins!")
                    break
                elif sum(dealers_card) > 21:
                    print("Dealer busted! You win!")
                    break
                elif sum(dealers_card) < 21:
                    # Compare totals to determine the winner
                    if total > sum(dealers_card):
                        print("You win!")
                        break
                    elif total < sum(dealers_card):
                        print("Dealer wins!")
                        break
            

# Main loop to allow replaying the games
while True:
    # Display game options to the user
    print("Hello! Would you like to play game 1 or 2?\n1. Guessing game\n2. Blackjack")

    try:
        # Get the user's choice of game
        choice = int(input("Your choice (one of the numbers):"))

        if choice in [1, 2]:
            # Start the chosen game
            if choice == 1:
                GuessingGame()
            elif choice == 2:
                Blackjack()

            # Ask if the user wants to play again
            replay = input("Would you like to play again? (y/n): ").lower()
            if replay != 'y':
                print("Thank you for playing! Goodbye!")
                break
    except ValueError:
        # Handle invalid input for game choice
        print("Invalid input. Please enter a number.")
