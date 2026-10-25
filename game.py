import random

# Words used in the game
WORDS = [
    "python", "computer", "programming",
    "developer", "keyboard", "student",
    "internet", "science", "college",
    "software"
]

# ASCII hangman stages
HANGMAN_STAGES = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


def display_word(word, guessed_letters):
    """Show guessed letters and hide the remaining letters."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("=" * 35)
    print("   HANGMAN WORD GUESSING GAME")
    print("=" * 35)

    while wrong_guesses < max_attempts:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word:", display_word(word, guessed_letters))
        print("Incorrect attempts left:",
              max_attempts - wrong_guesses)

        if guessed_letters:
            print("Guessed letters:",
                  ", ".join(sorted(guessed_letters)))

        guess = input("Enter one letter (or type quit): ")
        guess = guess.strip().lower()

        if guess == "quit":
            print("Game ended. The word was:", word)
            return

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!\n")
        else:
            wrong_guesses += 1
            print("Incorrect guess!\n")

        if all(letter in guessed_letters for letter in word):
            print(HANGMAN_STAGES[wrong_guesses])
            print("Word:", word)
            print("Congratulations! You won!")
            return

    print(HANGMAN_STAGES[max_attempts])
    print("You lost! The correct word was:", word)


if __name__ == "__main__":
    play_hangman()