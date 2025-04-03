import random

def guess(x):
    random_number = random.randint(1,x)
    user_guess = None
    attempts = 0

    print("\n🎯 Welcome to the 'Guess the Number' Game! 🎯")
    print(f"I have selected a number between 1 and {x}. Can yuo guess it?")

    while user_guess != random_number:
        try:
            user_guess = int(input("\nEnter Your guess: ")) 
            attempts += 1

            if user_guess < 1 or user_guess > x:
                print(f"🚨 Out of range! Please enter a number between 1 and {x}.")
            elif user_guess < random_number:
                print("📉 Too low! Try again.")
            elif user_guess > random_number:
                print("📈 Too high! Try again.")  
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
    print(f"\n🎉 Congratulations! You guessed the number {random_number} correctly in {attempts} attempts. 🏆")

    # Ask if the player wants to play again
    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again == ("yes"):
       guess(x)
    else:
        print("\nThanks for playing! Have a great day! 🥰")   
# Run the game with a chosen range or default (10)
if __name__ == "__main__":
    while True:
        try:
            upper_limit = input("\nEnter the upper limit for the guessing game (Press Enter for default 10):")
            if upper_limit == "":
                guess(10)
                break

            upper_limit = int(upper_limit)
            if upper_limit < 1 :
                print("⚠️ Please enter a positive number greater than 0.")
            else:
                guess(upper_limit)
                break
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")        

