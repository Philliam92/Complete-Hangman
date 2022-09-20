#Step 5
from replit import clear
import random
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import stages, logo
print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
old_guess = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}...")
    while guess in old_guess:
        print(f"You've tried {guess}, try a different letter!")
        guess = input("Guess a letter: ").lower()
    #Check guessed letter 
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong. Add guess to a repeat list
    if guess not in chosen_word and guess not in old_guess:
        old_guess += guess
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess} that's not in the word!\nYou lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE.")
            print("--------")
            print(f"Challenge word: {chosen_word.upper()}")
            print(f"Tried letters: {old_guess}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("YOU WIN!!")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])