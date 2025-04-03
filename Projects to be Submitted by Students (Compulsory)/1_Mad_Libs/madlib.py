import time

def madlibs():
    print("Welcome to the Mad Libs Adventure! Fill in the blanks to create an exciting story.\n")

    # Taking Input from the user
    name = input("Enter a name:")
    age = input("Enter an age:")
    city = input("Enter a city:")
    profession = input("Enter a profession:")
    mirical = input("Enter a mirical (e.g., prayers):")
    adjective1 = input("Enter an adjective:")
    adjective2 = input("Enter another adjective:")
    object1 = input("Enter a mysterious object: ")
    object2 = input("Enter another object:")
    angel = input("Enter an angel:")
    villain_name = input("Enter a villain's name:")
    verb = input("Enter an action verb:")

    # Story with user inputs
    story = f"""
     Once upon a time in the bustling city of {city}, there lived a {adjective1} {profession} named {name}.
    At just {age} years old, {name} was known an {angel} abilities.

    One day, while exploring an ancient library, {name} stumbled upon a {object1}.
    As soon as they touched it, a bright light surrounded them, and suddenly, a {mirical} appeared!
    The {mirical} told {name} that they were the chosen one to protect the city from the evil {villain_name}.

    Armed with courage and a {adjective2} {object2}, {name} set out on a thrilling adventure.
    Along the way, they encountered magical lands, solved mysterious riddles, and faced dangerous obstacles.

    Finally, the moment of truth arrived. {villain_name} was about to destroy {city}, but {name} call to ALLAH for their help
    , then an {angel} {verb} {villain_name}just in time, saving the city from destruction!

    The people of {city} cheered, and the {mirical} rewarded {name} with a lifetime of wisdom.
    forever... ✨

    THE END.
    """

    print("\nGenerating your story.....\n")
    time.sleep(2)  # Adding a dramatic pause for effect
    print(story)

# Running the Mad Libs Game
if __name__ == "__main__":
    madlibs()
