import pygame
import sys
import time  # Note this!
import hero_module
import cloud_module

def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    # DONE 1: Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode((1000, 600))

    # Done 2: Make a Clock
    clock = pygame.time.Clock()
    # Done 7: As a temporary test, make a new Raindrop called test_drop at x=320 y=10
    # test_drop = Raindrop(screen, 320, 10)
    # Done 15: Make a Hero, named mike, with appropriate images, starting at position x=200 y=400.
    mike = hero_module.Hero(screen, 200, 400, "Mike_umbrella.png", "Mike.png")
    # Done 15: Make a Hero, named alyssa, with appropriate images, starting at position x=700 y=400.
    alyssa = hero_module.Hero(screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")
    # Done 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    cloud = cloud_module.Cloud(screen, 300, 100, "another_cloud.png")

    # Done 3: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                # Done 4:   Make the pygame.QUIT event stop the game.

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cloud.y -= 5
        if pressed_keys[pygame.K_DOWN]:
            cloud.y += 5
        if pressed_keys[pygame.K_LEFT]:
            cloud.x -= 5
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x += 5

        # Done 27: Inside the game loop (AFTER the events loop above), get the list of keys that are currently pressed.
        #     Arrange so that the Cloud moves:
        #       5 pixels (or 10 pixels) to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        #       5 pixels (or 10 pixels) to the left  if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        #       5 pixels (or 10 pixels) up           if the Up    Arrow key (pygame.K_UP)    is pressed.
        #       5 pixels (or 10 pixels) down         if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        # DISCUSS: If you want something to happen once per key press, put it in the events loop above
        #          If you want something to continually happen while holding the key, put it after the events loop.

        # Done 5: Inside the game loop, draw the screen (fill with white)
        screen.fill((255,255,255))

        # --- begin area of test_drop code that will be removed later
        # Done 12: As a temporary test, move test_drop
        # test_drop.move()
        # # Done 14: As a temporary test, check if test_drop is off screen, if so reset the y position to 10
        # if test_drop.off_screen():
        #     test_drop.y = 10
        # # Done 10: As a temporary test, draw test_drop
        # test_drop.draw()

        # # Done 20: As a temporary test, check if test_drop is hitting Mike (or Alyssa), if so set their last_hit_time
        # if mike.hit_by(test_drop):
        #     mike.last_hit_time = time.time()
        #     test_drop.x = 700
        #     test_drop.y = 10
        # if alyssa.hit_by(test_drop):
        #     alyssa.last_hit_time = time.time()
        #     test_drop.x = 200
        #     test_drop.y = 10
        # Done 22: Remove the code that reset the y of the test_drop when off_screen()
        #          Instead reset the test_drop y to 10 when mike is hit, additionally set the x to 750
        #          Then add similar code to alyssa that sets her last_hit_time and moves the test_drop to 10 320
        # --- end area of test_drop code that will be removed later

        # Done 26: Draw the Cloud.
        cloud.draw()
        # Done 29: Remove the temporary testdrop code from this function and refactor it as follows:
        cloud.rain()
        for raindrop in cloud.raindrop_list:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrop_list.remove(raindrop)
            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrop_list.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrop_list.remove(raindrop)
        # Done: Make the Cloud "rain", then:
        # Done    For each Raindrop in the Cloud's list of raindrops:
            #       - move the Raindrop.
            #       - draw the Raindrop.
            # TODO  30: if the Hero (Mike or Alyssa) is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            # Optional  - if the Raindrop is off the screen or hitting a Hero, remove it from the Cloud's list of raindrops.

        # Done 18: Draw the Heroes (Mike and Alyssa)

        mike.draw()
        alyssa.draw()
        # Done 6: Update the display and remove the pass statement below
        pygame.display.update()

# Done 0: Call main.
main()