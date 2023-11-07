import time
import random
from threaded_button import *
from spi_screen import *

# Sample quotes (add more as needed)
SHAKESPEARE_QUOTES = [
    "My tongue will tell the anger of my heart, or else my heart concealing it will break",
    "All the world's a stage, and all the men and women merely players",
    "Love is merely a madness",
    "How can it be said that I am alone when all the world is here to look at me?",
    "My pride fell with my fortunes",
    "And yet, to say the truth, reason and love keep little company together nowadays",
    "Speak low, if you speak love",
    "I do believe her, though I know she lies",
    "True love never did run smooth",
    "And I'll stay... forgetting any other home but this",
    "All that glisters is not gold",
    "Men's eyes were made to look and let them gaze",
    "When I was at home, I was in a better place",
    "In black ink my love may still shine bright",
    "By the pricking of my thumbs, something wicked this way comes",
    "There is nothing either good or bad, but thinking makes it so",
    "These violent delights have violent ends",
    "My love as deep. The more I give, the more I have, for both are infinite.",
    "I will confess to you that I love him.",
    "Sad hours seem long",
    "He...shuts up his windows, locks fair daylight out, and makes himself an artificial night.",
    "You and I are past our dancing days",
    "The course of true love never did run smooth",
    "The greatest thing you'll ever learn is just to love and be loved in return.",
    "Love is not love which alters when it alteration finds"
    
    
    # Add more Shakespeare quotes...
]

TAYLOR_SWIFT_QUOTES = [
    "Did I close my fist around something delicate? Did I shatter you?",
    "Do you miss the rogue who coaxed you into paradise and left you there?",
    "Past the curses and cries, beyond the terror and the nightfall",
    "Now my eyes leak acid rain on the pillow where you used to lay your head",
    "I meet you where the spirit meets the bones, in a faith-forgotten land",
    "Your touch brought fourth an incandescent glow, tarnished but so grand",
    "Now you hang from my lips, like the gardens of Babylon",
    "I wish to know the flaw that makes you long to be magnificently cursed",
    "Take me to the lakes where all the poets went to die, I don't belong, and my beloved neither do you",
    "I sit here and wait, grieving for the living",
    "Staring out an open window, catching my death",
    "Can't not think of all the cost, and all that will be lost",
    "In the cracks of light, I dreamed of you",
    "All we are is skin and bone, trained to get along",
    "Did the twin flame bruise paint you blue?",
    "Falling feels like flying until the bone crush",
    "Is it romantic how all my elegies eulogize me?",
    "You are an expert at sorry and keeping the lines blurry",
    "I wounded the good and I trusted the wicked",
    "Eyes like sinking ships on water, I almost jump in",
    "You, with your swords and weapons that you use against me.",
    "I break free and leave us in ruins, take this dagger in me and remove it.",
    "I greet you with a battle hero's welcome."
    # Add more Taylor Swift quotes...
]

ALL_QUOTES = [(quote, "Shakespeare") for quote in SHAKESPEARE_QUOTES] + [(quote, "Taylor Swift") for quote in TAYLOR_SWIFT_QUOTES]

# Create instantiation of the buttons
        
class QuoteGame:
    def __init__(self):
        self.delay = 0.1
        self.finaldelay = 5
        self.gamedelay = 0.4
        self.startdelay = 2
        self.display = SPI_Display()
        time.sleep(self.delay)
        print("Shakespeare or Taylor Swift?")
        self.display.text(["Shakespeare", "or Taylor Swift?"], justify=CENTER, align=CENTER)
        time.sleep(self.startdelay)
        self.button_0 = ThreadedButton("P2_2") #shakespeare
        self.button_1 = ThreadedButton("P2_8")
        
        self.button_0.set_on_press_callback(self.guessShakespeare)
        self.button_1.set_on_press_callback(self.guessTaylor)
        
        self.button_0.start()
        self.button_1.start()
        
        self.guess_flag = True
        self.counter = 0
        self.total = 0
        

    def load_new_quote(self):
        self.current_quote, self.correct_answer = random.choice(ALL_QUOTES)
        print("\n" + self.current_quote)
        self.display.text("{0}".format(self.current_quote), justify=CENTER, align=CENTER, wrap=True)
        time.sleep(self.gamedelay)

    def guess(self, author):
        if author == self.correct_answer:
            print(f"That was indeed {self.correct_answer}!")
            self.display.text(["That was indeed", "{0}".format(self.correct_answer)], justify=CENTER, align=CENTER)
            time.sleep(self.gamedelay)
            self.counter = self.counter + 1
            self.total = self.total + 1
        else:
            print(f"That was a tricky one! It was actually {self.correct_answer}.")
            self.display.text(["That was a tricky one!", "It was actually", "{0}".format(self.correct_answer)], justify=CENTER, align=CENTER)
            time.sleep(self.gamedelay)
            self.total = self.total + 1
        self.guess_flag= True
        

    def run(self):
        
        while True:
            start_time = time.time()
            while time.time() - start_time < 60:
                if self.guess_flag == True:
                    self.load_new_quote()
                    print("\nChoose the author:")
                    print("1. Shakespeare")
                    print("2. Taylor Swift")
                    self.guess_flag= False
                time.sleep(0.1)
            time.sleep(3)    
            self.display.text(["Game Over!", "Your Score:", "{0} / {1}".format(self.counter,self.total)], justify=CENTER, align=CENTER)
            time.sleep(self.finaldelay)
            self.display.text(["Let's Play Again!","Shakespeare","or Taylor Swift?"], justify=CENTER, align=CENTER)
            time.sleep(self.startdelay)
            self.display.text("{0}".format(self.current_quote), justify=CENTER, align=CENTER, wrap= True)
            
            
            

    def guessShakespeare(self):
        self.guess("Shakespeare")

    def guessTaylor(self):
        self.guess("Taylor Swift")
        
if __name__ == "__main__":
    game = QuoteGame()
    game.run()