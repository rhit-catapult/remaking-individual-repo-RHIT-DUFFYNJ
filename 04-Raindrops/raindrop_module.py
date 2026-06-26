import pygame
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(6,8)
        # Done 8: Initialize this Raindrop, as follows:
        #     - Store the screen.
        #     - Set the initial position of the Raindrop to x and y.
        #     - Set the initial speed to a random integer between 5 and 15.
        #   Use instance variables:   screen  x  y  speed.

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        self.y += self.speed
        # Done 11: Change the  y  position of this Raindrop by its speed.

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        return self.y > self.screen.get_height()
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # Done 13: Return  True  if the  y  position of this Raindrop is greater than 800.

    def draw(self):
        """ Draws this sprite onto the screen. """
        pygame.draw.line(self.screen, (100,0,255), (self.x, self.y), (self.x, self.y + 5), 2)
        # Done 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        #      from the current position of this Raindrop (use either a black or blue color).