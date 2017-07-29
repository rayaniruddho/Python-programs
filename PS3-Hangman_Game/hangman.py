# Hangman game


import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    
    print("Loading word list from file...")
    
    inFile = open(WORDLIST_FILENAME, 'r')
    
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
   
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    
    value=False
    ans=list(secretWord)
    for i in range(len(ans)):
        if ans[i] in lettersGuessed:
            value=True
        else:
            value=False
            break
    return value



def getGuessedWord(secretWord, lettersGuessed):
    
    ans=list(secretWord)
    string=""
    for i in range(len(ans)):
        if ans[i] in lettersGuessed:
            string+=str(ans[i])
        else:
            string+="_ "
    return string



def getAvailableLetters(lettersGuessed):
    
    string="abcdefghijklmnopqrstuvwxyz"
    ans=""
    for l in string:
        if l not in lettersGuessed:
            ans+=l
    return ans
    

def hangman(secretWord):
    
    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 0
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + intro + ' letters long.')
    print('------------')
 
     
    while mistakesMade < 8:
        if isWordGuessed(secretWord,lettersGuessed):
            return print('Congratulations, you won!')
        print ('You have ' + str(8-mistakesMade) + ' guesses left.')
        print ('Available letters:' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter:').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print ('Oops! You\'ve already guessed that letter:' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print ('Good guess:' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ('Oops! You\'ve already guessed that letter:' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                mistakesMade += 1
                print ('Oops! That letter is not in my word:' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
    return print('Sorry, you ran out of guesses. The word was ' + secretWord)
                

        


secretWord = chooseWord(wordlist).lower()


hangman(secretWord)
