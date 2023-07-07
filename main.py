import pygame, sys
from pygame.locals import QUIT
from paddle import Paddle
from ball import Ball

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Initializers
pygame.init()
DISPLAYSURF = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Pong')

#Variables
score1 = 0
score2 = 0
clock = pygame.time.Clock()

#Sprites
paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 40
paddle1.rect.y = 200

paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 590
paddle2.rect.y = 200

ball = Ball(WHITE, 10)
ball.rect.x = 320
ball.rect.y = 240

spritelist = pygame.sprite.Group()
spritelist.add(paddle2)
spritelist.add(paddle1)

spritelist.add(ball)
#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #input
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_w]):
        paddle1.move(4)
    if (keys[pygame.K_s]):
        paddle1.move(-4)

    if (keys[pygame.K_UP]):
        paddle2.move(4)
    if (keys[pygame.K_DOWN]):
        paddle2.move(-4)

    #Collision
    if pygame.sprite.collide_mask(ball, paddle2) or pygame.sprite.collide_mask(
            ball, paddle1):
        ball.bounce()

    #Reset Check
    if ball.rect.x < 35:
        ball.reset()
        score2 += 1
        ball.velocityX = -6
    if ball.rect.x > 605:
        ball.reset()
        score1 += 1
        ball.velocityX = 6

    

    #Screen
    DISPLAYSURF.fill(BLACK)
    spritelist.update()
    spritelist.draw(DISPLAYSURF)
    pygame.draw.line(DISPLAYSURF, WHITE, [0, 0], [640, 0], 2)
    pygame.draw.line(DISPLAYSURF, WHITE, [0, 478], [640, 478], 2)
    pygame.draw.line(DISPLAYSURF, WHITE, [319, 0], [319, 480], 2)

    #Text Display
    font = pygame.font.Font(None, 70)
    text = font.render(str(score1), 1, WHITE)
    DISPLAYSURF.blit(text, (150, 40))

    text = font.render(str(score2), 1, WHITE)
    DISPLAYSURF.blit(text, (480, 40))
  
    clock.tick(60)  
    pygame.display.flip()
