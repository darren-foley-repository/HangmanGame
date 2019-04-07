from application import Hangman


def validateWord(string):
    """
    Returns true is the word is just a alphabetic string. Will return false if string contains numbers or other symbols
    """
    if string.isalpha() and " " not in string:
        return True
    print("That's not valid word, try again!")
    return False

if __name__ == "__main__":
    print(
    """Welcome to hangman!!
    
    """)
    hostName = str(input("Enter the host's name here: ")).lower()

    challengerName = str(input("Enter the challenger's name here: ")).lower()

    print(
    f"""Hey {hostName}!, enter your word below. Make sure {challengerName} isn't looking!!
    """)

    # Validate input string
    while(True):
        secret_word = input("Enter your word: ")
        if(validateWord(secret_word)):
            secret_word = secret_word.lower()
            break

    # Initiate the board
    board = Hangman(challengerName, hostName, secret_word)

    first=True
    # Start the game
    try:
        while board.challenger.guesses != 0:

            while(True):
                if first == False:
                    letter = input("Enter a letter or enter '!' to make a guess at the word: ")
                else:
                    letter = input("Enter a letter: ")

                if letter == "!" and first == False:
                    full_guess = input("ok, enter your full guess: ")
                    if validateWord(full_guess) and board.makeFullGuess(full_guess.lower()):
                        print(f"""
                        THATS CORRECT {board.challenger.name}!
                        
                        {full_guess} is the correct answer!!, YOU'VE WON!!
                        """)
                        raise StopIteration
                elif (board.validateLetter(letter)):
                    letter = letter.lower()
                    break

            print("""
            
            """)
            # Check if letter is in word
            if board.host.checkLetter(letter):
                print("Well done that was a correct guess!")
                board.addToCorrectGuesses(letter)
            else:
                print("That letter was not there!")
                board.addToWrongGuesses(letter)
                board.challenger.oneLess()

            board.hangmanState()
            if first:
                first = False
    except StopIteration as e:
        pass






