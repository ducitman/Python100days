import random
import requests
from nltk.corpus import words

# Download the word list (only need to do this once)
import nltk
nltk.download('words')

def choose_word():
    # Get the word list
    word_list = words.words()

    # Filter words based on your criteria
    valid_words = [word for word in word_list if 6 < len(word) < 12 and len(set(word)) <= 6]
    random_word = random.choice(valid_words)
    return random_word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def translate_to_vietnamese(word):
    url = "https://api.mymemory.translated.net/get"
    params = {"q": word, "langpair": "en|vi"}
    response = requests.get(url, params=params)
    
    # Kiểm tra phản hồi
    #print("Response JSON:", response.json())  # In ra phản hồi JSON
    return response.json()["responseData"]["translatedText"]


def hangman_game():
    word_to_guess = choose_word()
    meaning = translate_to_vietnamese(word_to_guess)
    #print(f"\n{meaning}")
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Hangman! Guess the word below:")
    print(display_word(word_to_guess, guessed_letters))

    while attempts_left > 0:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Correct! Attempts left: {attempts_left}")
        else:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("\n*****You Win*****")
            print(f"\nThe word was: {word_to_guess} - Meaning: {meaning}")
            break
    else:
        print(f"\nYou Lose! The word was: {word_to_guess} - Meaning: {meaning}")
        
        
if __name__ == "__main__":
    hangman_game()