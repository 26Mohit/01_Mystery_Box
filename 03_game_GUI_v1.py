from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance amd stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push Me", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)

    def to_game(self):

        # retrieve starting balance
        starting_balance = 50
        stakes = 1

        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # initialise variables
        self.balance = IntVar()

        # Set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Play...
        self.play_label = Label(self.game_frame, text="Play...",
                                font="Arial 24 bold", padx=10,
                                pady=10)
        self.play_label.grid(row=0)

        # Heading row
        self.heading_label = Label(self.game_frame, text="Press <enter> or click the 'Open Boxes' button to "
                                                         "reveal the contents of the mystery boxes.",
                                   font="Arial 12", padx=10, wrap=250,
                                   pady=10)
        self.heading_label.grid(row=1)

        # Balance Label
        self.balance_label = Label(self.game_frame, text="")
        self.balance_label.grid(row=1)

        self.play_button = Button(self.game_frame, text="?",
                                  padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

        # Balance Label
        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1, column=2)

        self.balance_label = Label(self.game_frame, text="")
        self.balance_label.grid(row=2)

        self.play_button = Button(self.game_frame, text="?",
                                  padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

        # Balance Label
        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1, column=3)

        self.balance_label = Label(self.game_frame, text="")
        self.balance_label.grid(row=2)

        self.play_button = Button(self.game_frame, text="?",
                                  padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

        # Open Boxes
        self.open_boxes_frame = Frame(self.game_frame)
        self.open_boxes_frame.grid(row=2)

        self.play_button = Button(self.game_frame, text="Open Boxes",
                                  font="Arial 18 bold",
                                  bg="#FFFF33",
                                  padx=20, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

    def reveal_boxes(self):

        # retrieve the balance from the initial function..
        current_balance = self.balance.get()

        # adjust the balance (subtract game cost and add pay out)
        # For testing purposes, just add 2
        current_balance +=2

        # Set balance to adjust balance
        self.balance.set(current_balance)

        # Edit label so user can see their balance
        self.balance_label.configure(text="Balance: {}".format(current_balance))

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    Start(root)
    root.mainloop()
