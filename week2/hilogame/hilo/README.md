# cse210-02

Name: Chris Mills
Email: admin@themillsclan.com

Title: Hilo Card Game
Description: The Hili Card Game is a game that asks a player to drawer a card and then guess if the next card will be a higher value or a lower value. If the player guesses correctly they are rewarded with 100 points, if they guess wrong then they loose 75 points.
A player can continue playing until they either choose to stop and keep their score, or they exhaust all their points.

Project Structure:
The project is seperated into 2 main classes with a __main__ program calling the neccessary classes into action.
player class:
    Attributes:
        is_playing (boolean): whether the game is currently playing
        score (int): the score for the current round of play
        card (obj): the current card being played
        lastCard (int): the previous card played
        highlow (int): 1 if the player guesses higher, 0 if they guess lower
    Methods:
        start_game:
            controls the flow of the game, checkng if the player is still playing
        get_inputs:
            accepts input from the user
        do_outputs
            prints the value of the card to the screen and checks if the player wants another turn
        do_updates:
            drawers a card, displays the card and checks if the user made a correct guess

card class:
    drawers a card from the deck of cards with a value of 1 to 13
    The responsibility of the card is to keep track of the value of the current card and to drawer a new card when needed.

    Attributes:
        value (int): the value of the current card
        points (int): the number of points in the current card

    Methods:
        drawer(self): drawers a new card and assign it to the card object
        show(self, message): displays the value of the current card with a specified message
Required software
    requires the random class
