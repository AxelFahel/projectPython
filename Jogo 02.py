'''
Code projeto visto em vídeos na internet
necessario instalar pip install pygame

'''

import pygame
pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
bird_image = pygame.image.load('bird.png')
bird_x = 50
bird_y = 250
pipe_top_image = pygame.image.load('pipe_top.png')
pipe_top_x = 400
pipe_top_y = -200
pipe_bottom_image = pygame.image.load('pipe_bottom.png')
pipe_bottom_x = 400
pipe_bottom_y = 400
GRAVITY = 0.2
bird_velocity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -5

bird_velocity += GRAVITY
bird_y += bird_velocity

pipe_top_x -= 2
pipe_bottom_x -= 2
if pipe_top_x < -100:
    pipe_top_x = 400
    pipe_top_y = random.randint(-400, -100)
    pipe_bottom_x = 400
    pipe_bottom_y = pipe_top_y + 600
if bird_x + 30 > pipe_top_x and bird_x < pipe_top_x + 100 and bird_y < pipe_top_y + 500:
    pygame.quit()
    sys.exit()
if bird_x + 30 > pipe_bottom_x and bird_x < pipe_bottom_x + 100 and bird_y + 30 > pipe_bottom_y:
    pygame.quit()
    sys.exit()

screen.fill(WHITE)
screen.blit(bird_image, (bird_x, bird_y))
screen.blit(pipe_top_image, (pipe_top_x, pipe_top_y))
screen.blit(pipe_bottom_image, (pipe_bottom_x, pipe_bottom_y))
pygame.display.update()

