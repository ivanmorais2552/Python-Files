import random

sChoices = ["rock", "paper", "scissors"]

iComputerScore = 0
iPlayerScore = 0


# Allows the player to choice their input. Print's "Invalid Choice!" if chosen input is not in the sChoices array.
def get_player_choice():
    playerChoice = input("Choose rock, paper, or scissors: ").lower()

    while playerChoice not in sChoices:
        print("Invalid choice!")
        playerChoice = input("Choose rock, paper, or scissors: ").lower()

    return playerChoice


# Gives the computer a random choice from the sChoices array.
def get_computer_choice():
    computerChoice = random.choice(sChoices)
    return computerChoice


# Determines the winner of each round.
def determine_winner(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        return "tie"
    elif ((playerChoice == "rock" and computerChoice == "paper")
          or (playerChoice == "paper" and computerChoice == "scissors")
          or (playerChoice == "scissors" and computerChoice == "rock")):
        return "loss"
    else:
        return "win"


# Main Game
print("\nWelcome to Rock Paper Scissors!")

iNumOfGames = int(
    input("How many rounds would you like to play?\n(Enter an odd number): ")
)

while iNumOfGames % 2 == 0:
    print("Sorry, the number must be an odd number.")
    iNumOfGames = int(
        input("How many rounds would you like to play?\n(Enter an odd number): ")
    )

iGamesPlayed = 0

while iGamesPlayed < iNumOfGames:
    playerChoice = get_player_choice()
    computerChoice = get_computer_choice()

    print(f"The computer chose {computerChoice}.")

    result = determine_winner(playerChoice, computerChoice)

    if result == "tie":
        print("Tie! Play again.")

    elif result == "win":
        print("You won!")
        iPlayerScore += 1
        iGamesPlayed += 1

    else:
        print("You lost!")
        iComputerScore += 1
        iGamesPlayed += 1


# Print's the results from the game
print("-------------------------------------------")
print(f"Score — You: {iPlayerScore} | Computer: {iComputerScore}")

if iPlayerScore > iComputerScore:
    print("You win!")
else:
    print("Computer wins! Better luck next time!")

print("Thanks for playing!")
