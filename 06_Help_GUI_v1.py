
from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Start:
    def __init__(self, parent):

        # start Main screen GUI...
        self.start_frame = Frame(width=600, height=600)
        self.start_frame.grid()

        # Mystery Box Heading (row 0)
        self.temp_start_label = Label(self.start_frame, text="Mystery Box Game",
                                      font="Arial 16 bold",
                                      padx=10, pady=10)
        self.temp_start_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.start_frame, text="Help", padx=10, pady=10,
                                  command=self.to_help)
        self.help_button.grid(row=1, pady=10)

    def to_help(self):
        get_help = Help(self)


class Help:
    def __init__(self,partner):

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (i.e: help box)
        self.help_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box)
        self.help_frame.grid()

        # Set up Help heading (row)
        self.how_heading = Label(self.help_frame,text="Help / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="Choose an amount to play with and then choose the stakes. "
                                                     "Higher stakes cost more per round but you can win more as " 
                                                     "well.\n\n"
                                                     "When you enter the play area, you will see three mustery "
                                                     "boxes. To reveal the contents of the oxes, click the "
                                                     "'Open Boxes' button. if don't have enough money to play, "
                                                     "the button will turn red and you will need to quite the "
                                                     "game.\n\n"
                                                     "The contents of the boxes will be added to your balance. "
                                                     "The boxes could contain...\n\n"
                                                     "Low: Lead ($0)  | Copper ($1) | Silver ($2) | Gold ($10)\n"
                                                     "Medium: Lead ($0)  | Copper ($2) | Silver ($4) | Gold ($25)\n"
                                                     "High: Lead ($0)  | Copper ($5) | Silver ($10) | Gold ($50)\n\n"
                                                     "If each box conains gold, you can earn $30 (low stakes). If "
                                                     "they contained copper, silver and gold, you would receive "
                                                     "$13 ($1 + $2 + $10) and so on.",
                               width=60, wrap=400)
        self.help_text.grid(row=1)

        # Dismiss button ( row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", font="Arial 15 bold",
                                  width=20, bg="#660000", fg="white",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    Start(root)
    root.mainloop()
