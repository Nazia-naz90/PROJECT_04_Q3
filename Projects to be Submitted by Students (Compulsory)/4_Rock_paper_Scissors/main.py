import random
import math

def play():
    """Handles a single round of Rock, Paper, Scissors."""
    user = input("\nWhat's your choice?  (r for Rock, p for Paper, s for Scissors):").strip().lower()

    while user not in ['r', 'p', 's']:
        print("❌ Invalid choice! Please enter 'r', 'p', or 's'.")
        user = input("Try again:").strip().lower()

    computer = random.choice(['r','p','s'])

    if user == computer:
        return (0 , user , computer)
    if is_win(user ,computer):
        return (1 , user , computer)
    return (-1 , user , computer) 

def is_win(player , opponent):
    """Returns True if the player beats the opponent , else False ."""
    winning_combinations = {'r':'s', 's':'p' , 'p':'r'}
    return winning_combinations[player] == opponent

def play_best_of(n):
    """Plays a  'best of N' sries until a winner is decided."""
    print("\n🎮 Welcome to Rock, Paper, Scissors! 🎮")
    print(f"First to win {math.ceil(n/2)} out of {n} games wins!\n")

    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)

    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result , user , computer = play()
        
        choices = {'r': 'Rock' , 'p': 'Paper' , 's': 'Scissors'}
        user_choice = choices[user]
        computer_choice = choices[computer]

        if result == 0:
           print(f"🤝 It's a tie! You both chose {user_choice}.\n")
        elif result == 1:
            player_wins += 1
            print(f"✅ You win! {user_choice} beats {computer_choice}.\n")
        else:
            computer_wins += 1
            print(f"❌ You lose! {computer_choice} beats {user_choice}.\n")
            

        print(f"🏆 Score: You {player_wins} | Computer {computer_wins}\n")

    if player_wins > computer_wins:
        print(f"🎉 Congratulations! You won the best of {n} games! 🏆")   

    else:
        print(f"😞 The computer won the best of {n} games. Better luck next time!")


    # Ask if the user wants to play again
    play_again = input("\nWould you like to play again? (yes/no):")
    if play_again == 'yes':
       play_best_of(n)
    else:
        print("Thanks for playing! See you next time. 😊")


# Run the game with best of 3
if __name__ == "__main__":
    play_best_of(3)
