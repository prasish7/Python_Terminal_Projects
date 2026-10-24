import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    return random.choice(words)
def display_word(word, guessed_letters):
    displayed = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return displayed
def check_guess(word, guessed_letters, guess):
    return guess in word

def hangman():
    counter = 6
    word = choose_word()
    guessed_letters = []


    while counter > 0:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if not check_guess(word, guessed_letters, guess):
            counter -= 1
            print("Wrong guess.")
        else:
            print("Good guess!")

    if display_word(word, guessed_letters) == word:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()