import pygame
import sys
import random
import math

def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    return math.sqrt((point2_x - point1_x)**2 + (point2_y - point1_y)**2)
class Ball(object):
    def __init__(self, coords_tuple, vel_tuple, screen):
        self.random_setup()
        self.set_coords(coords_tuple)
        self.set_vel(vel_tuple)
        self.is_held = False
        self.screen = screen

    def random_setup(self):
        base_color = [random.randint(0,50), random.randint(0,50), random.randint(0,50)]
        base_color[random.randint(0,2)] = random.randint(100,200)
        base_color[random.randint(0,2)] = random.randint(200,255)
        self.color = pygame.Color(base_color)

        self.radius =  random.randint(30,60)

    def get_center(self):
        return (self.x, self.y)
    
    def get_radius(self):
        return self.radius

    def held(self, value):
        self.is_held = value

    def get_held(self):
        return self.is_held
        
    def draw_circle(self):
        pygame.draw.circle(self.screen, pygame.Color(self.color), (self.x,self.y), self.radius)
    
    def set_coords(self, coords_tuple):
        self.x = coords_tuple[0]
        self.y = coords_tuple[1]

    def set_vel(self, vel_tuple):
        self.velx = vel_tuple[0]
        self.vely = vel_tuple[1]
    
    def apply_motion(self):
        self.x += self.velx
        self.y += self.vely
        self.vely = self.vely + 1

    def check_edges(self):
        self.dampening = 0.9
        if self.x > self.screen.get_width() - self.radius and self.velx > 0:
            self.velx = (-1 * self.velx) * self.dampening
        if self.x < self.radius / 2 and self.velx < 0:
            self.velx = (-1 * self.velx) * self.dampening
        if self.y > self.screen.get_height() - self.radius and self.vely > 0:
            self.vely = (-1 * self.vely + 1) * self.dampening
            self.velx = self.velx * (1 - (1 -self.dampening) / 5) 
        if self.y < self.radius / 2 and self.vely < 0:
            self.vely = (-1 * self.vely + 1) * self.dampening

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball (Try grabbing a ball)')
    clock = pygame.time.Clock()

    balls_list = []
    for ball in range(10): 
        ball = Ball((random.randint(200,700), random.randint(200,700)), (random.randint(-20,20), random.randint(-20,20)), screen)
        balls_list.append(ball)
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in balls_list:
                    if distance(ball.get_center(), pygame.mouse.get_pos()) <= ball.get_radius():
                        ball.held(True)
                        break

            if event.type == pygame.MOUSEBUTTONUP:
                for ball in balls_list:
                    if ball.get_held():
                        ball.set_vel(pygame.mouse.get_rel())
                        ball.held(False)

        #advance frame          
        pygame.mouse.get_rel()
        clock.tick(60)
        screen.fill(pygame.Color('white'))

        for ball in balls_list:
            if  ball.get_held():
                ball.set_coords(pygame.mouse.get_pos())       
            else:
                ball.check_edges()
                ball.apply_motion()
            ball.draw_circle() 

        pygame.display.update()
main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
