from game.card import Card

class Player:
    """ A person who directs the game.
    
    The responsibility of the player is to control the flow of the game

    Attributes:
        is_playing (boolean): whether the game is currently playing
        score (int): the score for the current round of play
        card (obj): the current card being played
        lastCard (int): the previous card played
        highlow (int): 1 if the player guesses higher, 0 if they guess lower
    """

    def __init__(self):
        """ Constructor. 
        Args: self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 300
        self.card = Card()
        self.lastCard = self.card
        self.highlow = 0
        self.card.drawer()
 
    def start_game(self):
        """ starts the game by running the main game loop.
        Args:
            self (Player): an instance of Player.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            if not self.is_playing:
                print(f'Your final score is {self.score}')
                return 

    def get_inputs(self):
        """Ask the user if they want to guess higher or lower.
        Args:
            self (Player): An instance of Player.
        """
        self.card.show("The current card is a")
        self.highlow = int(input("Higher (1) or Lower (0): "))
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Player): An instance of Player.
        """
        self.lastCard = self.card.value
        self.card.drawer()
        self.card.show("You drew a ")

        if (self.highlow == 1 and self.lastCard < self.card.value) or (self.highlow == 0 and self.lastCard > self.card.value):
            self.score += 100
        else:
            self.score -= 75

        if self.score <= 0:
            self.is_playing = False

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to go again. 

        Args:
            self (Player): An instance of Player.
        """
              
        print(f"Your score is: {self.score}\n")
        # self.is_playing == (self.score > 0)  
        if self.is_playing:
            self.is_playing = True if input("Play again? [y/n]: ") == "y" else False     