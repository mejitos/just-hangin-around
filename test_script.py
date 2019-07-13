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
fail_words = []
games = 0
counter = 0
success = 0
fail = 0

# Get the list of all the words with length of word_length
with open('fails8char.txt', 'r', encoding='utf-8') as word_file:
    content = word_file.readlines()
    for word in content:
        # if len(word.replace('\n', '')) >= 6 and len(word.replace('\n', '')) <= 8:
        if len(word.replace('\n', '')) == 8:
            words.append(word.replace('\n', '').upper())

clear_screen()
print('~~~~~ H _ N G M _ N ~~~~~')
print()
print_hangman()
print(f'Word length: 8')
print(f'Words: {len(words)}')
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
    # the_word = words[random.randint(0, len(words) - 1)]
    the_word = words[counter]
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

    print(histogram)
    # for key in sorted(histogram.keys()) :
    #     print(key , ' : ', histogram[key])
    # print(sorted(histogram, key=histogram.get))
    for c in sorted(histogram, key=histogram.get, reverse=True):
        print(c, histogram[c]
)
    # Print the secret word on screen and start the game
    print('~ ~ ~ ~ ~ H _ N G M _ N ~ ~ ~ ~ ~')
    print(f'Game #{counter + 1}')
    print(f'Secret Word: {the_word}')
    # print(remaining_words)
    # print(histogram)
    print('- - - - - - - - - - - - - - - - - - - - - -')

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

        # print(f'Guesses: {" ".join(guesses)}')


        # collections.Counter => most_common
        # Start guessing with the most common character
        max_val = max(histogram.values())
        the_char = ''

        for k in histogram:
            if histogram[k] == max_val:
                the_char = k.upper()
                guesses.append(the_char)
                break

        # Computer makes guess
        # print(f'Strikes: {strikes}')
        # print(f'Algorithm guess: "{the_char}"')

        answer = ''

        if the_char in the_word:
            answer = 'yes'
        else:
            answer = 'no'

        # print(f'Char in word: {answer}')

        if answer == 'yes':
            while True:
                for i in range(0, len(the_word)):
                    if the_word[i] == the_char:
                        empty_word[i] = the_char
                        indexes.append(i)
                        indexes.sort()
                
                for i in indexes:
                    if the_word[i] == empty_word[i]:
                        if i == indexes[len(indexes) - 1]:
                            answer = 'yes'
                        pass
                    else:
                        answer = 'no'
                        break

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

            # print(remaining_words)

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
            
            # print(histogram)

        # Eliminate all the words which has wrongly guessed char in them
        else:
            for word in reversed(remaining_words):
                if the_char in word:
                    remaining_words.remove(word)
            
            # print(remaining_words)

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

            # print(histogram)

            strikes += 1

    # -------------------- MAIN LOOP ENDS HERE -------------------------

    # -------------------- MAKING GUESS OF THE WORD -------------------------

    # this based on 6-8 character words
    # make a guess after 4 chars are known and/or only x-amount of words is left?
    # if like only three words are left => guess randomly
    # else check all the remaining words for common chars to try out end exclude
    # print('-------- GUESSING STARTS ---------')

    while True:

        if strikes == 6:
            break
        
        guess = remaining_words[random.randint(0, len(remaining_words) - 1)]

        # print(f'Computer guess: {guess}')
        
        if the_word == guess:
            answer = 'yes'
        else:
            answer = 'no'

        # print(answer)

        if answer == 'yes':
            break
        else:
            remaining_words.remove(guess)
            strikes += 1
            if strikes == 6 or len(remaining_words) == 0:
                break

    if strikes == 6:
        fail += 1
        fail_words.append(the_word)
        print('player wins')
    else:
        success += 1
        print('computer wins!')
    
    counter += 1

# with open('fails.txt', 'w', encoding='utf-8') as f:
#     for word in fail_words:
#         f.write(word + '\n')

print('~~~~~~~~~~ END ~~~~~~~~~~')
print()
print(f'played {games} games')
print('results:')
print(f'player {fail} - computer {success}')