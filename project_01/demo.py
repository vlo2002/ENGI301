import random
from threaded_button import *

# Sample quotes (add more as needed)
SHAKESPEARE_QUOTES = [
    "To be, or not to be: that is the question.",
    "All the world's a stage, and all the men and women merely players.",
    # Add more Shakespeare quotes...
]

TAYLOR_SWIFT_QUOTES = [
    "But I've got a blank space, baby. And I'll write your name.",
    "You belong with me.",
    "Take me to the lakes where all the poets went to die, I don't belong, and my beloved neither do you."
    # Add more Taylor Swift quotes...
]

ALL_QUOTES = [(quote, "Shakespeare") for quote in SHAKESPEARE_QUOTES] + [(quote, "Taylor Swift") for quote in TAYLOR_SWIFT_QUOTES]

# Create instantiation of the buttons


class QuoteGame:
    def __init__(self):
        print("Shakespeare or Taylor Swift?")
        self.button_0 = ThreadedButton("P2_2") #shakespeare
        self.button_1 = ThreadedButton("P2_8")
        
        self.button_0.set_on_press_callback(self.guessShakespeare)
        self.button_1.set_on_press_callback(self.guessTaylor)
        
        self.button_0.start()
        self.button_1.start()
        
        self.guess_flag = True
        

    def load_new_quote(self):
        self.current_quote, self.correct_answer = random.choice(ALL_QUOTES)
        print("\n" + self.current_quote)

    def guess(self, author):
        if author == self.correct_answer:
            print(f"That was indeed {self.correct_answer}!")
        else:
            print(f"That was a tricky one! It was actually {self.correct_answer}.")
        self.guess_flag= True
        

    def run(self):
        
        while True:
            if self.guess_flag == True:
                self.load_new_quote()
                print("\nChoose the author:")
                print("1. Shakespeare")
                print("2. Taylor Swift")
                self.guess_flag= False
            
            time.sleep(0.1)

    def guessShakespeare(self):
        self.guess("Shakespeare")

    def guessTaylor(self):
        self.guess("Taylor Swift")

if __name__ == "__main__":
    game = QuoteGame()
    game.run()