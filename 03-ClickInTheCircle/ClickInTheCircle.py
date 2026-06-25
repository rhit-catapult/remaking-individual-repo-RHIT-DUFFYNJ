import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    return math.sqrt((point2_x - point1_x)**2 + (point2_y - point1_y)**2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)

    # TODO 8: Load the "drums.wav" file into the pygame music mixer
    pygame.mixer.music.load("drums.wav")

    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    circle_color = (154, 58, 212)
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 3

    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if distance(circle_center, pygame.mouse.get_pos()) <= circle_radius:
                    pygame.mixer.music.play(-1)
                    message_text = "Hit"
                else:
                    message_text = "Miss"
                    pygame.mixer.music.stop()


                # TODO 9: Start playing the music mixer looping forever if the click is within the circle
                # TODO 10: Stop playing the music if the click is outside the circle

        screen.fill(pygame.Color("Black"))

        pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)
        message_caption = font.render(message_text, True, (122, 237, 201))
        screen.blit(message_caption, (20, 360))

        screen.blit(instructions_image, (25, 25))

        pygame.display.update()


main()