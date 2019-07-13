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
Added script to use for testing the algorithm I have and by using that, I'm going to try to make my algorithm better. Theres two scripts now, one "basic" version and other that uses multiprocessing. I'm trying to make my algorithm better one word length at a time, but exectuing test script for 5.6k words with 8 characters in length, it would take over 10 minutes to execute so that isn't that helpful. With simple multiprocessing I get down to 3-4 minutes. Script will load all the words from the wordlist and make them into wordsets which have maximum of 1000 words. Each of these wordsets will be assigned its own process.

## The Algorithm
**Ruleset**
* You can have five strikes before game over, sixth strike == game over
* You can guess the secret word as many times as you want but wrong guess gives strikes += 1

**You choose your word's length. If your secret word is "banana", there is six characters so your word length is six**
* Algorithm will choose remaining words only with words that has six characters
* At this point algorithm will only know word "_ _ _ _ _ _ "
* Algorithm iterates through the characters of the remaining words making a historgram out of them which it uses to see the frequencies of the characters

**Main loop**
* Algorithm will make a guess with the most common character and appends it to "guessed_chars" list
* Check if guessed characters >= 4 characters, if yes, break the loop
* Check if number of remainig words is between 1-3, if yes, break the loop
* If guessed character (e.g. 'A') is in the secret word:
    * You need to tell the indexes of all the characters are in the secret word e.g. "_ A _ A _ A".
    * Algorithm iterates through the remaining words removing words that doesn't have guessed character on given indexes and updates histogram accordingly
* Else:
    * Algorithm will iterate through the remaining words removing words that doesn't have the guessed character
    * Algorithm iterates through the remaining words removing words that doesn't have guessed character on given indexes and updates histogram accordingly

**Main loop ends**

**Ending**
* Algorithm will make guess by choosing random word from the remaining words

## Results
Algorithm was basically just changed so that it executes main loop until only one word remains and it did surprisingly well. Did a lot of refactoring of the code as well but sadly it didn't affect the performance at all.

### 8 character words
- Success rate: 99.77%
- Failed 10 / 5643 words

#### Failed words
'HUOVUTUS', 'HYLLYKKÖ', 'HYPPYNEN', 'YÖTÖN YÖ', 'PYÖRÖPUU', 'PÖLLÖNEN', 'HARJANNE', 'MUUNTELU', 'KOLMONEN', 'ROPPONEN'

### 7 character words
- Success rate: 98.83%
- Failed 47 / 4343 words

#### Failed words
'MAHAVYÖ,','JONOTUS','JOROTUS','JULUPPI','JÄÄNNÖS','JÄÄTELÖ','JÖPÖTYS','RÄTVÄNÄ','MERSAWA','VIEMÄRI','MOLOTUS','MUSUKKI','MÖKÖTYS','XÂRÂCÙÙ','B-DUURI','YÖPÖLLÖ','B-MOLLI','BUNTŠUK','ÖLJYPUU','C-DUURI','SLOWFOX','SLUUPPI','NUKUPUU','NUORUUS','DISPARI','KLÖNTTI','F-DUURI','FIMOOSI','F-MOLLI','PERKELE','PERKELE','KUUPÖLY','GIBBONI','KYYHKYT','KYYNÄRÄ','TERVEYS','PINSERI','POM-POM','POROTUS','PUMPULI','TUNGPUU','HURJUUS','TYHMYRI','PYSÄKKI','HYPPYRI','TYÖKYKY','PÖKKELÖ'

### 6 character words
- Success rate: 96.05%
- Failed 129 / 3389 words

#### Failed words
'TRYMOO','KELVIN','VAGHUA','PLYYMI','PLÄKKI','KOMEDO','POLTOS','POLTTO','POMELO','KOOKOS','BABUZA','KOOLON','KOOSTO','PONCHO','POPPOO','PORROT','PORTTO','POTERO','KORSTO','BICHON','KOSMOS','KOSSOT','BINOMI','PROFFA','BLONDI','PRUNNI','BLOSSI','BLUFFI','BLÄÄGÄ','BOLERO','VENÄJÄ','PUHURI','BONOBO','BORŠTŠ','BREVIS','BUNDIS','CHINOS','CONTRA','PYLVÄS','COWBOY','KURSSI','PYÖKKI','DEMONI','PÄRSTÄ','PÄÄRLY','PÄÄRME','VOODOO','PÖLLÖT','PÖNKKÄ','DIRNDL','PÖNTTÖ','DIVEHI','QUELLI','KYHÄRI','VÄLKKÄ','VÄLPPÄ','VÄRKKI','DREENI','VÄÄNTÖ','DUELLI','KÄMPPÄ','EEMELI','EFENDI','KÄÄNTÖ','ÄÄNNÖS','LEMMIÖ','LEMURI','RYNNÄS','FLOORA','RÄÄKKI','RÄÄPPÄ','FRENDI','RÄÄTTI','RÖMPSÄ','FYNBOS','FÄDÄRI','FÄGÄRI','FÄRSSI','FÖNÄRI','GIGOLO','GUELFI','GÖÖTTI','HALAUS','LUUPPI','LÄHÄRI','SFÄÄRI','LÄMÄRI','LÄÄKIS','LÖRPPÖ','LÖÖPPI','HEMPPO','HEPULI','HEŠVÁN','HINKKI','HORROS','HUHMAR','MILJÖÖ','SOLJOT','MOGULI','HYYPPÄ','SOTKOS','HÄKÄRÄ','HÄMÄRÄ','HÄRKIN','HÄRKKI','HÖMPPÄ','HÖMPSY','HÖNTSÄ','HÖRPPY','HÖRTSÖ','MYRTTI','MÄNNYT','MÄYRIS','ŠUNTTI','SYDÄRI','NELSON','JEEPPI','JENKKI','JEPARI','JOHDOS','JULPPI','NORKKO','JURUMI','JYMINÄ','JÄKÄLÄ','JÄLKKÄ','JÄRKKÄ','NYRKKI','OBADJA'