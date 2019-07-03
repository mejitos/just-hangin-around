# Just Hangin' Around

Little game of hangman where you can play with yourself or let the computer try to guess your word.

For now the game works on finnish words only and both versions of the game has hardcoded stuff all around it.
- CPU has hardcoded word length of 7 characters
- The normal version for now is pretty horrible but its somewhat playable
- Neither of the versions have any bugfixes or validations
- As a bonus there is big lists of finnish substantives, adjectives and verbs if someone needs them for something. Didn't find any from the internet so I made my own by scraping.

# hangin.py
This is the "normal" version of the game. Game gets a random word from the database and your mission is to try to guess to right word by giving right characters or the right word.

# CPU script
When using this script, you are supposed to write your word on a piece of paper and after that, the script tries to guess your word. It asks for characters and their places in the string and you can input the characters with numbers.

# Testing script
Added script to use for testing the algorithm I have and by using that, I'm going to make my algorithm better. For now as it simplest state it makes guesses only based on frequency of characters in the words and still makes right guesses ~80% of the time.

To use the script, you only need to have list of words and then you input the number of games you want to play and go at it.