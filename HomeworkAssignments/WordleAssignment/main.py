import wordle_functions as wf

# Welcome the player and explain the feedback
print("Welcome to Mystery Wordle!")
print("Guess the five-letter word.")
print("🟩 = correct letter and position")
print("🟨 = correct letter, wrong position")
print("- = letter is not in the word")

# Repeat the game until the player chooses to stop
while True:
    round_counter = 1
    pastGuesses = []
    secretWord = wf.choose_word()

    # Allow up to six attempts
    while round_counter <= 6:
        print(f"\nAttempt {round_counter} of 6")

        guess = wf.get_guess()

        # Prevent duplicate guesses
        if guess in pastGuesses:
            print("You guessed that already!")
            continue

        pastGuesses.append(guess)

        # Evaluate and display feedback
        feedback = wf.evaluate_guess(guess, secretWord)
        print(wf.display_guess(guess, feedback))

        # Check whether the player won
        if wf.has_won(guess, secretWord):
            print("\nCongratulations! You solved the puzzle.")
            break

        round_counter += 1

    else:
        # The player used all six attempts
        print("\nYou Lose. Sorry!")
        print("The secret word was:", "".join(secretWord))

    # Ask whether the player wants to play again
    playAgain = input("Would you like to play again? ").lower()

    if playAgain == "no":
        print("Thanks for playing!")
        break
