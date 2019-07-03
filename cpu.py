import random
import os

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


# Setup the game

word_length = 7
empty_word = []
inputs = []
words = []
guesses = []
# remaining_words = []
indexes = []
histogram = {}
strikes = 0

clear_screen()
print('~~~~~ H _ N G M _ N ~~~~~')
print()
print('lets play a game of hangman')
print('write a word between 6-8 characters on paper')
# TODO: This gives the word length => saved to word_length variable, hardcoded for now
print('how many characters does your word have?')
input('6 - 8 characters > ')
# TODO: Option to choose word class => saved to word_class variable, hardcoded for now
print('what is the word class?')
input('substantive / adjective / verb > ')

# Get the list of all the words with length of word_length
with open('substantiivit.txt', 'r', encoding='utf-8') as word_file:
    content = word_file.readlines()
    for word in content:
        if len(word.replace('\n', '')) == word_length:
            words.append(word.replace('\n', ''))

empty_word = ['_' for i in range(word_length)]
inputs = [str(i + 1) for i in range(word_length)]

# Make a histogram of all the letters of the selected words in database
for word in words:
    for char in word:
        if char not in histogram:
            histogram[char] = 1
        else:
            histogram[char] += 1

# Print the secret word on screen and start the game
clear_screen()
print('~~~~~ H _ N G M _ N ~~~~~')
print()
print_hangman(strikes)
print(' '.join(empty_word))
print()
input('start the game by pressing ENTER >')


# -------------- MAIN LOOP STARTS HERE -----------------
while True:
    # Check for guessed characters and remaining words
    # if guessed characters == 4 or more => break
    # if remaining words == 1-4 => break
    guessed_chars = 0
    for c in empty_word:
        if c != '_':
            guessed_chars += 1
    if word_length - guessed_chars <= 3:
        break
    if len(words) >= 1 and len(words) <= 4:
        break

    # Start guessing with the most common character
    max_val = max(histogram.values())
    the_char = ''

    for k in histogram:
        if histogram[k] == max_val:
            the_char = k
            guesses.append(the_char)
            break

    # Computer makes guess
    clear_screen()
    print('~~~~~ H _ N G M _ N ~~~~~')
    print()
    print_hangman(strikes)
    print(' '.join(empty_word))
    print()
    print(f'does the word have character "{the_char}"? > ')

    # TODO: Validate the yes or no
    answer = input('yes / no > ')
    print()

    if answer == 'yes':
        while True:
            # Ask from the user where the letters are in the secret word
            clear_screen()
            print('~~~~~ H _ N G M _ N ~~~~~')
            print()
            print_hangman(strikes)
            print(' '.join(empty_word))
            print(' '.join(inputs))
            print()

            # TODO: Validation here to confirm the char placement?
            index = int(input('where the character is on the word? > '))
            indexes.append(index - 1)
            indexes.sort()
            print()

            # TODO: Validation here to confirm the char placement?
            empty_word[index - 1] = the_char

            clear_screen()
            print('~~~~~ H _ N G M _ N ~~~~~')
            print()
            print_hangman(strikes)
            print(' '.join(empty_word))
            print(' '.join(inputs))
            print()
            print(f'is that all the character {the_char}´s in the word?')

            # TODO: Validation here
            answer = input('yes / no > ')
            if answer ==  'no':
                pass
            else:
                # TODO: Last validation here to confirm all the correct chars and ask yes or no
                break

        # Check for all the words that have guessed characters on
        # and change the list of remaining words accordingly        
        for word in reversed(words):
            for i in indexes:
                if word[i] == empty_word[i]:
                    pass
                else:
                    words.remove(word)
                    break

        # Make a new histogram of all the characters of the remaining words
        histogram = {}
        for word in words:
            for char in word:
                if char in guesses:
                    pass
                elif char not in histogram:
                    histogram[char] = 1
                else:
                    histogram[char] += 1
    
    # Eliminate all the words which has wrongly guessed char in them
    else:
        for word in reversed(words):
            if the_char in word:
                words.remove(word)
        
        # Make a new histogram of all the characters of the remaining words
        histogram = {}
        for word in words:
            for char in word:
                if char in guesses:
                    pass
                elif char not in histogram:
                    histogram[char] = 1
                else:
                    histogram[char] += 1
        
        strikes += 1

# -------------------- MAIN LOOP ENDS HERE -------------------------

# -------------------- MAKING GUESS OF THE WORD -------------------------

# this based on 7 character words
# make a guess after 4 chars are known and/or only x-amount of words is left?
# if like only three words are left => guess randomly
# else check all the remaining words for common chars to try out end exclude

while True:
    if strikes == 6:
        break
    
    guess = words[random.randint(0, len(words) - 1)]

    clear_screen()
    print('~~~~~ H _ N G M _ N ~~~~~')
    print()
    print_hangman(strikes)
    print(f'is the word you are looking for "{guess}"?')
    answer = input('yes / no > ')

    if answer == 'yes':
        break
    else:
        words.remove(guess)
        strikes += 1
        if strikes == 6 or len(words) == 0:
            break

if strikes == 6 or len(words) == 0:
    print('player wins')
else:
    print('computer wins!')