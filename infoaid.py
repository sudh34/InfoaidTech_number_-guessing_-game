import random

def welcome():
    print("Welcome to the Number Guessing Game!")
    name = input("What's your name? ")
    print(f"Hello, {name}! Let's play a game.")
    print("I'm thinking of a number between 1 and 100. Can you guess it within 10 attempts?")

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < 10:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations, you guessed the number {secret_number} correctly in {attempts} attempts!")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    if user_guess != secret_number:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

def play_again():
    return input("Do you want to play again? (yes/no) ").lower() == 'yes'

if __name__ == "__main__":
    while True:
        welcome()
        play_game()
        
        if not play_again():
            print("Thanks for playing! Goodbye.")
            break
