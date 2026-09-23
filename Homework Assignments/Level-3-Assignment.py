import random

# Generate the secret number and track guesses
randomNum = random.randint(1, 100)
iCounter = 1

print("\nI'm thinking of a number between 1 and 100.\n")

# Continue until the player guesses correctly
while True:
    iGuess = int(input("Enter your guess: "))

    if iGuess < 1 or iGuess > 100:
        print("Error: Enter a number between 1 and 100.")
        continue

    if iGuess > randomNum:
        print("\nYour guess is too high. Guess lower.")
        iCounter += 1

    elif iGuess < randomNum:
        print("\nYour guess is too low. Guess higher.")
        iCounter += 1

    else:
        print(f"\nYou guessed it in {iCounter} tries!")

        # Give feedback based on the number of guesses
        if iCounter <= 3:
            print("Amazing!")
        elif iCounter <= 5:
            print("Impressive!")
        elif iCounter <= 7:
            print("Good job!")
        elif iCounter <= 9:
            print("Took a little longer, but you got there!")
        else:
            print("You need to lock in")

        # Ask whether the player wants to play again
        if input("\nWould you like to play again? (Y/N): ").lower() == "y":
            randomNum = random.randint(1, 100)
            iCounter = 1
            print("\nI'm thinking of a number between 1 and 100.\n")
        else:
            print("Thanks for playing!")
            break