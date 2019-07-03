import random
import os


def print_hangman():
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


def clear_screen():
    os.system('cls')


words = []
games = 0
counter = 0
success = 0
fail = 0

# Get the list of all the words with length of word_length
with open('substantiivit.txt', 'r', encoding='utf-8') as word_file:
    content = word_file.readlines()
    for word in content:
        if len(word.replace('\n', '')) >= 6 and len(word.replace('\n', '')) <= 8:
            words.append(word.replace('\n', ''))

clear_screen()
print('~~~~~ H _ N G M _ N ~~~~~')
print()
print_hangman()
print('lets test a game of hangman')
games = int(input('how many games you want to play through? > '))
print()

while counter < games:
    # Setup the game
    empty_word = []
    inputs = []
    guesses = []
    remaining_words = []
    indexes = []
    histogram = {}
    strikes = 0

    # Get the secret word
    # the_word = 'kokkare'
    the_word = words[random.randint(0, len(words) - 1)]
    empty_word = ['_' for i in range(len(the_word))]
    inputs = [str(i + 1) for i in range(len(the_word))]

    # Make a histogram of all the letters of the selected words in database
    for word in reversed(words):
        if len(word) != len(the_word):
            pass
        else:
            for char in word:
                if char not in histogram:
                    histogram[char] = 1
                else:
                    histogram[char] += 1
            remaining_words.append(word)

    # Print the secret word on screen and start the game
    print('~~~~~ H _ N G M _ N ~~~~~')
    print()
    print(f'Secret Word: {the_word}')

    # -------------- MAIN GAME LOOP STARTS HERE -----------------
    while strikes < 6:
        # Check for guessed characters and remaining words
        # if guessed characters == 4 or more => break
        # if remaining words == 1-4 => break
        guessed_chars = 0
        for c in empty_word:
            if c != '_':
                guessed_chars += 1
        if len(the_word) - guessed_chars <= 3:
            break
        if len(remaining_words) >= 1 and len(remaining_words) <= 4:
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
        print(f'Strikes: {strikes}')
        print()
        print(' '.join(empty_word))
        print()
        print(f'does the word have character "{the_char}"? > ')
        print()

        answer = ''

        if the_char in the_word:
            answer = 'yes'
        else:
            answer = 'no'

        print(answer)
        print()

        if answer == 'yes':
            while True:
                # Ask from the user where the letters are in the secret word
                print('where the character is on the word? > ')
                print()

                for i in range(0, len(the_word)):
                    if the_word[i] == the_char:
                        empty_word[i] = the_char
                        indexes.append(i)
                        indexes.sort()

                print(' '.join(empty_word))
                print(' '.join(inputs))
                print()

                print(f'is that all the character {the_char}´s in the word?')
                
                for i in indexes:
                    if the_word[i] == empty_word[i]:
                        if i == indexes[len(indexes) - 1]:
                            answer = 'yes'
                        pass
                    else:
                        answer = 'no'
                        break

                print(answer)
                print()

                if answer ==  'no':
                    pass
                else:
                    break

            # Check for all the words that have guessed characters on
            # and change the list of remaining words accordingly
            for word in reversed(remaining_words):
                for i in indexes:
                    if word[i] == empty_word[i]:
                        pass
                    else:
                        remaining_words.remove(word)
                        break

            # Make a new histogram of all the characters of the remaining words
            histogram = {}
            for word in remaining_words:
                for char in word:
                    if char in guesses:
                        pass
                    elif char not in histogram:
                        histogram[char] = 1
                    else:
                        histogram[char] += 1
            
        # Eliminate all the words which has wrongly guessed char in them
        else:
            for word in reversed(remaining_words):
                if the_char in word:
                    remaining_words.remove(word)
            
            # Make a new histogram of all the characters of the remaining words
            histogram = {}
            for word in remaining_words:
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

    # this based on 6-8 character words
    # make a guess after 4 chars are known and/or only x-amount of words is left?
    # if like only three words are left => guess randomly
    # else check all the remaining words for common chars to try out end exclude

    while True:
        if strikes == 6:
            break
        
        guess = remaining_words[random.randint(0, len(remaining_words) - 1)]

        print(f'is the word you are looking for "{guess}"?')
        
        if the_word == guess:
            answer = 'yes'
        else:
            answer = 'no'

        print(answer)
        print()

        if answer == 'yes':
            break
        else:
            remaining_words.remove(guess)
            strikes += 1
            if strikes == 6 or len(remaining_words) == 0:
                break

    if strikes == 6 or len(remaining_words) == 0:
        fail += 1
        print('player wins')
        print()
    else:
        success += 1
        print('computer wins!')
        print()
    
    counter += 1

print('~~~~~~~~~~ END ~~~~~~~~~~')
print()
print(f'played {games} games')
print('results:')
print(f'player {fail} - computer {success}')