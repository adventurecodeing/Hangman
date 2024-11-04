import random

# List of words for the game
word_list = ["python", "hangman", "challenge", "programming", "computer", "science"]

def select_word():
    return random.choice(word_list).lower()

def display_word_state(word, correct_guesses):
    display = [letter if letter in correct_guesses else "_" for letter in word]
    return " ".join(display)

def hangman_game():
    word = select_word()
    correct_guesses = set()
    incorrect_guesses = set()
    attempts_remaining = 6

    print("Welcome to Hangman Challenge!")
    print(f"The word has {len(word)} letters. You have {attempts_remaining} incorrect attempts available.")

    while attempts_remaining > 0:
        print("\n" + display_word_state(word, correct_guesses))
        print(f"Incorrect Guesses: {', '.join(incorrect_guesses)}")
        print(f"Attempts Remaining: {attempts_remaining}")
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in correct_guesses or guess in incorrect_guesses:
            print("You have already guessed that letter.")
            continue

        if guess in word:
            correct_guesses.add(guess)
            if all(letter in correct_guesses for letter in word):
                print(f"\nCongratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses.add(guess)
            attempts_remaining -= 1
            print(f"Wrong guess! {guess} is not in the word.")

        if attempts_remaining == 0:
            print(f"\nGame Over! The word was: {word}")

# Run the game
hangman_game()
