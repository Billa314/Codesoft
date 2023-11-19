#MUHAMMAD BILAL
#Rock-Paper-Scissor

import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while True:
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            return 'user'
        else:
            return 'computer'

    def display_result(self, user_choice, computer_choice, result):
        print(f'You chose {user_choice}. Computer chose {computer_choice}.')
        if result == 'tie':
            print("It's a tie!")
        elif result == 'user':
            print('You win!')
            self.user_score += 1
        else:
            print('Computer wins!')
            self.computer_score += 1
        print(f'Score: You {self.user_score} - Computer {self.computer_score}')

    def play_again(self):
        return input("Do you want to play again? (yes/no): ").lower() == 'yes'

    def play_game(self):
        print("Welcome to Rock, Paper, Scissors!")
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            result = self.determine_winner(user_choice, computer_choice)
            self.display_result(user_choice, computer_choice, result)
            if not self.play_again():
                print("Thanks for playing!")
                break

# Run the game
game = RockPaperScissorsGame()
game.play_game()
