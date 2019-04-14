import tkinter as tk
#from application import Hangman
from PIL import Image, ImageTk

class HangmanApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.pastGuessCorrect = []
        self.pastGuessIncorrect = []
        self.title("Hangman Game")
        self.geometry("500x500")
        self.counter = 3
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (StartPage, HostPage, ChallengerPage, LosePage, WinPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        if self.counter == 3:  # Call from Hangman init
            frame = self.frames[cont]
            frame.tkraise()
            self.counter -= 1
        elif self.counter == 2:
            frame = self.frames[cont]
            frame.tkraise()
            self.counter -= 1
        elif self.counter == 1:
            if self.checkHostWord() == False:
                frame = self.frames[HostPage]
                frame.tkraise()
            else:
                frame = self.frames[cont]
                frame.tkraise()
                self.counter -= 1
        else:  # Call from ChallengerPage init
            frame = self.frames[cont]
            self.checkLetterGuess()
            self.updateHangmanImage()
            self.updateWordLabel()

            frame.tkraise()
            # More checks and validation here

            #print(self.get_challenger_name())
            #print(self.get_host_name())
            #print(self.get_secret_word())
            #print(self.get_challenger_guess())

    def updateHangmanImage(self):
        number_of_guesses = len(self.pastGuessIncorrect)

        my_frame = self.frames[ChallengerPage]
        my_frame.my_image_number = number_of_guesses

        # change image
        my_frame.canvas.itemconfig(my_frame.image_on_canvas, image=my_frame.my_images[my_frame.my_image_number])


    def updateWordLabel(self):
        """
        Function used to print out input as user is making guesses
        """
        temp = ""
        for letter in self.get_secret_word().lower():
            if letter in self.pastGuessCorrect:
                temp += letter
            else:
                temp += "-"
        #self.frames[ChallengerPage].word_label = tk.Label(self.frames[ChallengerPage], text=temp)
        self.frames[ChallengerPage].text.set(temp)

    def checkHostWord(self):
        """
        Simple word validation function
        """
        word = self.get_secret_word()
        for letter in word:
            if letter.isalpha():
                continue
            else:
                print("This is not a valid word! Try again")
                return False
        return True


    def checkLetterGuess(self):
        letter = self.get_challenger_guess()
        word = self.get_secret_word()

        if letter.isalpha():
            letter = letter.lower()
            if letter in word.lower():
                print("Well done, that was a correct guess!")
                self.updateCorrectGuess(letter)
            else:
                print("That was not a correct guess")
                self.updateIncorrectGuess(letter)
        else:  # If the user input is not alphabetical
            print("Not valid input,....... one guess lost")
            self.updateIncorrectGuess(letter)

    def get_challenger_name(self):
        return self.frames[StartPage].challenger_name.get()

    def get_host_name(self):
        return self.frames[StartPage].host_name.get()

    def get_secret_word(self):
        return self.frames[HostPage].secret_word.get()

    def get_challenger_guess(self):
        return self.frames[ChallengerPage].guess.get()

    def updateIncorrectGuess(self, letter):
        self.pastGuessIncorrect.append(letter)

    def updateCorrectGuess(self, letter):
        self.pastGuessCorrect.append(letter)



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Welcome to Hangman! Please enter your details below...")
        label.pack()

        load = Image.open("images/hangman.gif")
        load = load.resize((250, 250), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        hangman_pic = tk.Label(self, image=render)
        hangman_pic.image = render
        hangman_pic.pack(side="bottom", fill="both")

        self.challenger_name = tk.Entry(self)
        self.challenger_name.insert(0, "Challengers name here!")
        self.challenger_name.pack()

        self.host_name = tk.Entry(self)
        self.host_name.insert(0, "Host name here!")
        self.host_name.pack()

        button = tk.Button(self, text="SUBMIT", command=lambda: controller.show_frame(HostPage))
        button.pack()



class HostPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Hey Host, enter a word!")
        label.pack()

        self.secret_word = tk.Entry(self)
        self.secret_word.insert(0, "Word")
        self.secret_word.pack()

        button = tk.Button(self, text="SUBMIT", command=lambda: controller.show_frame(ChallengerPage))
        button.pack()


"""
Data from the host page must be passed through to the challenger page
Data from the start page must be passed through to the challenger page also
"""
class ChallengerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Hey Challenger, enter a letter or enter a guess!")
        label.grid(row=0, column=0)

        self.guess = tk.Entry(self)
        self.guess.insert(0, "None")
        self.guess.grid(row=1, column=0)

        # canvas for image
        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.grid(row=2, column=0)

        # images
        self.my_images = []
        self.my_images.append(self.resizeImage("images/hangman_noguess.png"))
        self.my_images.append(self.resizeImage("images/hangman_oneguess.png"))
        self.my_images.append(self.resizeImage("images/hangman_twoguess.png"))
        self.my_images.append(self.resizeImage("images/hangman_threeguess.png"))
        self.my_images.append(self.resizeImage("images/hangman_fourguess.png"))
        self.my_images.append(self.resizeImage("images/hangman_fiveguess.png"))
        self.my_images.append(self.resizeImage("images/hangman_sixguess.png"))
        self.my_images.append(self.resizeImage("images/hangman_sevenguess.png"))
        self.my_images.append(self.resizeImage("images/hangman_eightguess.png"))
        self.my_images.append(self.resizeImage("images/hangman_lose.png"))
        self.my_image_number = 0

        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.my_images[self.my_image_number])

        self.text = tk.StringVar()
        self.word_label = tk.Label(self, textvariable=self.text)
        self.word_label.grid(row=3, column=0)

        button = tk.Button(self, text="SUBMIT", command=lambda: controller.show_frame(ChallengerPage))
        button.grid()


    def resizeImage(self, image_path):
        image = Image.open(image_path)
        image = image.resize((250, 250), Image.ANTIALIAS)  # The (250, 250) is (height, width)
        return ImageTk.PhotoImage(image)

    def printWord(self):
        return "-".join(i for i in range(0, len(self.text)+1))



class LosePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="You've been hung. You lose!!")
        label.grid(row=0, column=0)




class WinPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller





if __name__ == "__main__":
    app = HangmanApp()
    app.mainloop()

