# BENJI GOURDJI
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random
used_letters = []
correct_guesses = 0
incorrect_guesses = 0
done = False
word_list = ["quat", "anonymity", "cat", "theoretical", "artist", "kleptomaniac", "wand", "ytterbium", "statistically", "blockage"]
random_word = word_list[random.randrange(len(word_list))]
spaces = len(random_word)

while not done:
    print(hangmanpics[incorrect_guesses])
    print("used letters: ", used_letters)
    for char in random_word:
        if char in used_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")
    # prompt the user to guess a letter
    guess = (input("\n\nguess a letter: "))
    # if the guess is correct increment correct_guesses by 1
    if guess in used_letters:
        print("you already guessed that.")
    if guess.lower() in random_word:
        correct_guesses += 1
        used_letters.append(guess)
        print(guess.lower())
    else:
        incorrect_guesses += 1
        used_letters.append(guess)
        if guess.lower() not in used_letters:
            print(hangmanpics[incorrect_guesses])
    if incorrect_guesses >= 6:
        print("No. You lost.")
        done = True
    if correct_guesses == len(random_word):
        print("You Win")
        done = True