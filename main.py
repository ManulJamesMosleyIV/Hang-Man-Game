import random

from hangman_words import word_list

lives = 6
current_lives = lives
from hangman_art import stages



chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
already_guessed = []

while not game_over:

    print(f"You have {current_lives} current lives left.")

    guess = input("Guess a letter: ").lower()


    if guess in already_guessed:
        print(f"You already guessed {guess}, please try again.")
    else:
        already_guessed.append(guess)
    display = ""






    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        #elif guess in correct_letters:
                #print("you have already selected that letter, please try again")
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        current_lives = lives




        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print(f"You were trying to guess {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])

