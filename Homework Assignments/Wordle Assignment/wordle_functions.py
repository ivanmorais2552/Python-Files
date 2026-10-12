import random

words = [
    "apple", "brave", "chair", "dance", "eagle",
    "flame", "grape", "house", "image", "joker",
    "knife", "lemon", "magic", "night", "ocean",
    "piano", "queen", "river", "smile", "tiger",
    "urban", "vivid", "water", "youth", "zebra",
    "beach", "bread", "cloud", "dream", "earth",
    "field", "giant", "happy", "ivory", "juice",
    "koala", "light", "music", "noble", "olive",
    "peace", "quick", "radio", "stone", "train",
    "unity", "voice", "whale", "yield", "storm",
    "adopt", "blaze", "crane", "drift", "elbow",
    "fancy", "ghost", "hotel", "input", "jelly",
    "known", "lucky", "metal", "never", "orbit",
    "paint", "quiet", "roast", "sharp", "trust",
    "under", "visit", "wheat", "xerox", "young",
    "actor", "block", "charm", "doubt", "enjoy",
    "fresh", "globe", "honor", "issue", "kneel",
    "laugh", "march", "nurse", "organ", "plant",
    "route", "sugar", "theme", "upper", "vital",
    "worry", "extra", "crisp", "fairy", "sword"
]


# Chooses a random word and puts the individual letters into a list.
def choose_word():
    randomWord = random.choice(words).upper()
    return list(randomWord)


# Selects and returns a correct word (Word with only letters and length of 5). Puts the individual letters into a list.
def get_guess():
    guess = input("Enter a 5 letter word: ").upper()
    while not guess.isalpha() or len(guess) != 5:
        print("Invalid input!")
        guess = input("Enter a 5 letter word: ").upper()
    return list(guess)


# Starts result as a list of "-". Example: ["-","-","-","-","-"]. It sets remainingLetters as an equal list to the secretWord. Than it goes through the guess, looking at the index values and comparing those to the secretWord index values. If it results in a G, it replaces the matching remainingLetters value with a None, so that isn't used again in the evaluation. Same for the Y and if nothing it stays as a -.
def evaluate_guess(guess, secretWord):
    result = ["-"] * len(guess)
    remainingLetters = list(secretWord)
    for i in range(len(guess)):
        if guess[i] == secretWord[i]:
            result[i] = "G"
            remainingLetters[i] = None
    for i in range(len(guess)):
        if result[i] != "G" and guess[i] in remainingLetters:
            result[i] = "Y"
            remainingLetters[remainingLetters.index(guess[i])] = None
    return result


# Displays the guess as G U E S S.
def display_guess(guess, feedback):
    guessFormatted = " ".join(guess)
    feedbackFormatted = " ".join(feedback)
    return f"Guess: {guessFormatted}\nFeedback: {feedbackFormatted}"


# Returns true if guess == secretWord.
def has_won(guess, secretWord):
    return guess == secretWord
