import pygame
import random  # Note this!
import raindrop_module

class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        self.screen =screen
        self.x = x
        self.y = y
        self.cloud_image = pygame.image.load(image_filename)
        self.raindrop_list = []
        # Done 24: Initialize this Cloud, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Cloud to x and y.
        #     - Set the image of this Cloud to the given image filename.
        #     - Create a list for Raindrop objects as an empty list called raindrops.
        #   Use instance variables:
        #      screen  x  y  image   raindrops.


    def draw(self):
        """ Draws this sprite onto the screen. """
        # Done 25: Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.cloud_image,(self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        for _ in range(5):
            drop_x = random.randint(self.x + 30, self.x + self.cloud_image.get_width() - 30)
            drop_y = self.y + self.cloud_image.get_height()-10
            new_raindrop = raindrop_module.Raindrop(self.screen, drop_x, drop_y)
            self.raindrop_list.append(new_raindrop)
            # Done 28: Append a new Raindrop to this Cloud's list of raindrops,
            #     where the new Raindrop starts at:
            #       - x is a random integer between this Cloud's x and this Cloud's x + 300.
            #       - y is this Cloud's y + 100.
