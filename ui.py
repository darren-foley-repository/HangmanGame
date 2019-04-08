import tkinter as tk
from PIL import Image, ImageTk

class HangmanApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Hangman Game")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (StartPage, HostPage, ChallengerPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to Hangman! Please enter your details below...")
        label.pack()

        load = Image.open("C:/Users/DarrenFoley/PycharmProjects/HangmanGame/images/hangman.gif")
        render = ImageTk.PhotoImage(load)
        hangman_pic = tk.Label(self, image=render)
        hangman_pic.image = render
        hangman_pic.place(x=0, y=0)

        challenger_name = tk.Entry(self)
        challenger_name.insert(0, "Challengers name here!")
        challenger_name.pack()

        host_name = tk.Entry(self)
        host_name.insert(0, "Host name here!")
        host_name.pack()

        button = tk.Button(self, text="SUBMIT", command=lambda: controller.show_frame(HostPage))
        button.pack()



class HostPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hey Host, enter a word!")
        label.pack()

        secret_word = tk.Entry(self)
        secret_word.insert(0, "Enter your word here!")
        secret_word.pack()

        button = tk.Button(self, text="SUBMIT", command=lambda: controller.show_frame(ChallengerPage))
        button.pack()



class ChallengerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Hey Challenger enter a letter or enter a guess!")
        label.pack()

        button = tk.Button(self, text="SUBMIT", command=lambda: controller.show_frame(ChallengerPage))
        button.pack()









if __name__ == "__main__":
    app = HangmanApp()
    app.mainloop()

