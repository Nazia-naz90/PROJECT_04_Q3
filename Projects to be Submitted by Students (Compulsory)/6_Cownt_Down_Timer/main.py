import time
import sys

def countdown(t): 
    
    """Runs the countdown timer for the given seconds."""
    print("\n⏳ Timer Started!\n")

    while t:
        mins, secs = divmod(t,60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f"\r⏳ {timer}", end="", flush=True)
        time.sleep(1)
        t -= 1
    print("\r⏳ 00:00 - Timer Completed! 🎉 ")
    time.sleep(1)    
    
    # Optional: Beep sound after timer ends (for Windows)
    if sys.platform.startswith("win"):
        import winsound
        winsound.Beep(1000,500) # Frequency = 1000 Hz, Duration = 500 ms
    # Ask if the user wants to restart the timer
    restart = input("\n🔄 Would you like to restart the timer? (yes/no):").strip().lower()   
    if restart in ["yes","y"]:
         start_timer()
    else:
        print("\n✅ Thanks for using the Countdown Timer! Have a great day! 😊")

def start_timer():
    """Handles user input and start the countdown."""
    while True:
        try:
            t = int(input("\n⏲️ Enter the countdown time in seconds: "))
            if t <= 0 :
                print("⚠️ Please enter a positive number greater than 0 .")
                continue
            countdown(t)
            break

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

# Run the timer
if __name__ == "__main__":
    start_timer() 