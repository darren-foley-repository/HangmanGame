
class Player(object):
    """
    Default Player object with a name
    """
    def __init__(self, playername):
        self.name = playername

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val


class Host(Player):
    """
    Player responsible for creating the word. If the challenger is unable to guess the word within 8 turns the host wins.
    """
    def __init__(self, hostname, hostword=""):
        Player.__init__(self, hostname)
        self.word = hostword

    @property
    def word(self):
        return self.__word

    @word.setter
    def word(self, val):
        self.__word = val

    def checkLetter(self, letter):
        if letter in self.word:
            return True
        return False


class Challenger(Player):
    """
    Player responsible for guessing the word. If he/she is unable to guess in the answer in 8 wrong guesses they lose. They get to try a letter each turn.
    """
    def __init__(self, challengename):
        Player.__init__(self, challengename)
        self.guesses = 8

    def oneLess(self):
        if self.guesses != 0:
            self.guesses = self.guesses - 1
        else:
            print("No more guesses left")

    @property
    def guesses(self):
        return self.__challengerguesses

    @guesses.setter
    def guesses(self, val):
        self.__challengerguesses = val



class Hangman(object):

    def __init__(self, challengerName, hostName, secret_word):
        self.challenger = Challenger(challengerName)
        self.host = Host(hostName, secret_word)
        self.pastGuessesCorrect = []
        self.pastGuessesWrong = []
        self.board = self.hangmanState()

    @property
    def challenger(self):
        return self.__challenger

    @challenger.setter
    def challenger(self, obj):
        self.__challenger = obj

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, obj):
        self.__host = obj

    def makeFullGuess(self, full_guess):
        if full_guess == self.host.word:
            return True

    def addToWrongGuesses(self, letter):
        self.pastGuessesWrong.append(letter)

    def addToCorrectGuesses(self, letter):
        self.pastGuessesCorrect.append(letter)

    def validateLetter(self, letter):
        if letter.isalpha() and " " not in letter:
            return True
        elif letter not in self.pastGuessesCorrect and letter not in self.pastGuessesWrong:
            return True
        print("That's not valid letter, try again!")
        return False

    def wordPrinter(self):
        temp = ""
        for lett in self.host.word:
            if lett not in self.pastGuessesCorrect:
                temp += "-"
            else:
                temp += lett
        return temp

    def hangmanState(self):

        if self.challenger.guesses == 8:
            print(f"""
            Guesses Left: {self.challenger.guesses}


            ______
            {self.wordPrinter()}
         """)

        elif self.challenger.guesses == 7:
            # First wrong Guess
            print(f"""
            Guesses Left: {self.challenger.guesses}
            ______
            |
            |
            |
            |
            |
            |
            |_____
            {self.wordPrinter()}
            """)

        elif self.challenger.guesses == 6:
            # Second wrong turn
            print(f"""
            Guesses Left: {self.challenger.guesses}
            ______
            |
            |    O
            |
            |
            |
            |
            |_____
            {self.wordPrinter()}
            """)

        elif self.challenger.guesses == 5:
            # Third wrong turn
            print(f"""
            Guesses Left: {self.challenger.guesses}
            ______
            |
            |    O
            |    |
            |    |
            |
            |
            |_____
            {self.wordPrinter()}
            """)

        elif self.challenger.guesses == 4:
            # Fourth turn
            print(f"""
            Guesses Left: {self.challenger.guesses}
            ______
            |
            |    O
            |   /|
            |    |
            |
            |
            |_____
            {self.wordPrinter()}
            """)

        elif self.challenger.guesses == 3:
            # Fifth turn
            print(f"""
            Guesses Left: {self.challenger.guesses}
            ______
            |
            |    O
            |   /|\\
            |    |
            |
            |
            |_____
            {self.wordPrinter()}
            """)

        elif self.challenger.guesses == 2:
            # Sixth turn
            print(f"""
            Guesses Left: {self.challenger.guesses}
            ______
            |
            |    O
            |   /|\\
            |    |
            |   / 
            |
            |_____
            {self.wordPrinter()}
            """)

        elif self.challenger.guesses == 1:
            # Seventh turn
            print(f"""
            Guesses Left: {self.challenger.guesses}
            ______
            |
            |    O
            |   /|\\
            |    |
            |   / \\
            |
            |_____
            {self.wordPrinter()}
            """)

        else:
            # Eigth wrong turn (Game ends, challenger loses)
            print(f"""
            
            SORRY {self.challenger.name}, YOU LOSE!!!!!
            YOU ARE HANGED!!
            
            Guesses Left: {self.challenger.guesses}
            ______
            |    |
            |    O
            |   /|\\
            |    |
            |   / \\
            |
            |_____
            {self.wordPrinter()}
            """)






