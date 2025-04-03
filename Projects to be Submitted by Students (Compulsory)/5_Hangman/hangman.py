import random
words = [ "apple", "fruit", "ball", "toy",  "cat","animal", "dog", "pet","egg","food","fish", "swim", "goat", "farm", "hat", "wear", "ice","cold", "jump", "move", "jump", "move",   "kite", "fly","lion", "moon", "nest", "owl", "pen","queen", "rain", "sun","hot",  "tree", "plant",  "umbrella",
"van","vehicle","water", "fox","yarn","zoo",   
    ]

word = random.choice(words)
guessed_letters = []
attempts = 7

print("Welcome to hangman game project!")
print("_" * len(words))

while attempts > 0 :
    guess = input("\n Guess the letters:").lower()

    if len(guess) != 1 or not guess.isalpha():
       print("Write one alphabet only!")
       continue
    if guess in guessed_letters:
       print("This letter is already guess choose another letter.")  
       continue
    guessed_letters.append(guess)

    if guess in word:
       print("Correct guess!") 
    else:
        attempts -= 1
        print(f"Wrong {attempts} attempts.")

    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)

    if "_" not in displayed_word:
        print(f"Congratulation! the correct word is : {word}")
        break
else:
    print(f"Game Over! the correct word is: {word}")                  