import random
import os


# print all the images
def print_pole():
    print('        =======xx')
    print('        |      ||')
    print('               ||')
    print('               ||')
    print('               ||')
    print('               ||')
    print('              /||')
    print('     ########//||#')
    print('    ########//#||##')
    print('    #################')
    print('      #############')
    print()
    print()


def strike_one():
    print('        =======xx')
    print('        |      ||')
    print('        0      ||')
    print('               ||')
    print('               ||')
    print('               ||')
    print('              /||')
    print('     ########//||#')
    print('    ########//#||##')
    print('    #################')
    print('      #############')
    print()
    print()


def strike_two():
    print('        =======xx')
    print('        |      ||')
    print('        0      ||')
    print('        !      ||')
    print('               ||')
    print('               ||')
    print('              /||')
    print('     ########//||#')
    print('    ########//#||##')
    print('    #################')
    print('      #############')
    print()
    print()


def strike_three():
    print('        =======xx')
    print('        |      ||')
    print('        0      ||')
    print('      ;"!      ||')
    print('               ||')
    print('               ||')
    print('              /||')
    print('     ########//||#')
    print('    ########//#||##')
    print('    #################')
    print('      #############')
    print()
    print()


def strike_four():
    print('        =======xx')
    print('        |      ||')
    print('        0      ||')
    print('      ;"!";    ||')
    print('               ||')
    print('               ||')
    print('              /||')
    print('     ########//||#')
    print('    ########//#||##')
    print('    #################')
    print('      #############')
    print()
    print()


def strike_five():
    print('        =======xx')
    print('        |      ||')
    print('        0      ||')
    print('      ;"!";    ||')
    print('      _/"      ||')
    print('               ||')
    print('              /||')
    print('     ########//||#')
    print('    ########//#||##')
    print('    #################')
    print('      #############')
    print()
    print()


def last_strike():
    print('        =======xx')
    print('        |      ||')
    print('        0      ||')
    print('      ;"!";    ||')
    print(r'      _/"\_    ||')
    print('               ||')
    print('              /||')
    print('     ########//||#')
    print('    ########//#||##')
    print('    #################')
    print('      #############')
    print()
    print()


def print_hangman(strikes):
    if strikes == 0:
        print_pole()
    elif strikes == 1:
        strike_one()
    elif strikes == 2:
        strike_two()
    elif strikes == 3:
        strike_three()
    elif strikes == 4:
        strike_four()
    elif strikes == 5:
        strike_five()
    elif strikes == 6:
        last_strike()


def clear_screen():
    os.system('cls')


words = []
chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z', 'Å', 'Ä', 'Ö']
guesses = []
strikes = 0
win = False

# Get length of the word
# TODO: Validation
word_length = int(input('how long is the word? > '))

# Get the secret word
with open('substantiivit.txt', 'r', encoding='utf-8') as word_file:
    content = word_file.readlines()
    for word in content:
        if len(word.replace('\n', '')) == word_length:
            words.append(word.replace('\n', ''))
word = words[random.randint(0, len(words) - 1)].upper()
empty_word = ['_' for i in range(len(word))]

# Game loop starts here
while True:
    # Check for game over
    if strikes == 6:
        break
    if '_' not in empty_word:
        win = True
        break

    # Update screen
    clear_screen()
    print('~~~~~ H _ N G M _ N ~~~~~')
    print()
    print_hangman(strikes)
    print(' '.join(empty_word))
    print()

    # Ask player input (guess a letter or guess a word)
    guess = input('make a guess (letter or word) and press enter > ').upper()
    print()

    # Validate user input
    if len(guess) == 1 or guess == word:
        # Update the game state
        if guess == word:
            win = True
            break
        elif guess in guesses:
            print('you have guessed that already')
            print()
            input('press enter to continue')
        elif guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    empty_word[i] = guess
            chars.remove(guess)
            guesses.append(guess)
        else:
            print('nope')
            print()
            input('press enter to continue')
            chars.remove(guess)
            guesses.append(guess)
            strikes += 1
    else:
        print('invalid input')
        print()
        input('press enter to continue')

# Game ending
if win:
    clear_screen()
    print('~~~~~ H _ N G M _ N ~~~~~')
    print()
    print_hangman(strikes)
    print(' '.join(empty_word))
    print()
    if guess == word:
        print(f'correct word was indeed {guess}')
    else:
        print(f'correct word was indeed {"".join(empty_word)}')
    print()
    print('you win the game')
    print()
else:
    clear_screen()
    print('~~~~~ H _ N G M _ N ~~~~~')
    print()
    print_hangman(strikes)
    print(' '.join(empty_word))
    print()
    print('too many wrong guesses')
    print(f'correct word was {word}')
    print()
    print('you lost the game')
    print()

# Exit the game
input('exit the game by pressing enter')