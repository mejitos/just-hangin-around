import random
import os
import time
from multiprocessing import Process, current_process, Array, Value


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

def let_it_hang(words, wordset, success, fail):
    fail_words = []
    success.value = 0
    fail.value = 0

    print(f'Process ID: {os.getpid()}')
    print(f'Process Name: {current_process().name}')

    for the_word in wordset:
        # Setup the game
        empty_word = ['_' for i in range(len(the_word))]
        guesses = []
        remaining_words = []
        indexes = []
        histogram = {}
        strikes = 0

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

            # collections.Counter => most_common
            # Start guessing with the most common character
            max_val = max(histogram.values())
            the_char = ''

            for k in histogram:
                if histogram[k] == max_val:
                    the_char = k.upper()
                    guesses.append(the_char)
                    break

            if the_char in the_word:
                answer = 'yes'
            else:
                answer = 'no'

            if answer == 'yes':
                for i in range(0, len(the_word)):
                    if the_word[i] == the_char:
                        empty_word[i] = the_char
                        indexes.append(i)
                indexes.sort()

                # Check for all the words that have guessed characters on
                # indexes of the indexes list and change the list of 
                # remaining words accordingly
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

        # ------------------ MAKING GUESS OF THE WORD ----------------------
        while True:
            if strikes == 6:
                break
            
            # Making guess by randomly choosing word from remaining words
            guess = remaining_words[random.randint(0, len(remaining_words) - 1)]

            if the_word == guess:
                answer = 'yes'
            else:
                answer = 'no'

            if answer == 'yes':
                break
            else:
                remaining_words.remove(guess)
                strikes += 1
                if strikes == 6 or len(remaining_words) == 0:
                    break

        if strikes == 6 or len(remaining_words) == 0:
            fail.value += 1
            # print('Computer loses')
        else:
            success.value += 1
            # print('Computer wins!')


if __name__ == '__main__':
    # clear_screen()

    word_length = 8
    all_words = []
    wordsets = []
    wordset = []
    processes = []
    success = Value('i', 0)
    fail = Value('i', 0)

    # Get the list of all the words with length of word_length
    # and assing them to wordsets with max length of 1000 words
    with open('substantiivit.txt', 'r', encoding='utf-8') as word_file:
        content = word_file.readlines()
        for word in content:
            if len(wordset) == 1000:
                wordsets.append(wordset)
                wordset = []
            if len(word.replace('\n', '')) == word_length:
                all_words.append(word.replace('\n', '').upper())
                wordset.append(word.replace('\n', '').upper())
        wordsets.append(wordset)

    print('~~~~~ H _ N G M _ N ~~~~~')
    print()
    print_hangman()
    print('Lets test a game of hangman')
    print(f'Word Class: Substantives')
    print(f'Word Length: {word_length}')
    print(f'Word Sets: {len(wordsets)}')
    print(f'Total Words: {len(all_words)}')
    # print(f'Total Words: {len([word for wordset in wordsets for word in wordset])}')
    print()
    input('Start the test by pressing Enter > ')
    print()

    start_time = time.time()

    print('Assignin processess...')
    print()
    print(f'CPUS: {os.cpu_count()}')

    # for wordset in wordsets:
    #     process = Process(target=let_it_hang, args=(all_words, wordset, success, fail))
    #     processes.append(process)

    #     process.start()
    
    # for process in processes:
    #     process.join()

    # for i in range(3):
    #     process = Process(target=let_it_hang, args=(all_words, wordset, success, fail))
    #     processes.append(process)

    #     process.start()
    
    # for process in processes:
    #     process.join()
    
    let_it_hang(all_words, wordset, success, fail)

    # with open('fails.txt', 'w', encoding='utf-8') as f:
    #     for word in fail_words:
    #         f.write(word + '\n')

    end_time = time.time()

    print()
    print('~~~~~~~~~~ END ~~~~~~~~~~')
    print()
    print(f'Script took {end_time - start_time} seconds')
    print(f'Played {len(all_words)} games')
    print(f'Computer succeeded {success.value} times')
    print(f'Computer failed {fail.value} times')