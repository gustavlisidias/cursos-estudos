import string


alph = string.ascii_lowercase


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for i in secretWord:
        if i in lettersGuessed:
            count += 1
        else:
            return False

    if count == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    corGuessed = ''
    for i in secretWord[:]:
        if i in lettersGuessed:
            corGuessed += i
        else:
            corGuessed += '_ '
            
    return corGuessed
             

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remain = []
    for i in alph:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)
            

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), "letters long.")

    mistakesMade = 0
    lettersGuessed = []

    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('Congratulations, you won!')
            break
        else:
            print('------------')
            print('You have', 8 - mistakesMade, 'guesses left.')
            print('Available letters:', getAvailableLetters(lettersGuessed))
            guess = str(input('Please guess a letter:')).lower()

            if guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))

            elif guess in lettersGuessed:
                print("Oops! You've already guessed that letter:",
                getGuessedWord(secretWord, lettersGuessed))

            elif guess not in secretWord:
                print("Oops! That letter is not in my word:",
                getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(guess)
                mistakesMade += 1

            if 8 - mistakesMade == 0:
                print('------------')
                print('Sorry, you ran out of guesses. The word was', secretWord)
                break
            
            else:
                continue