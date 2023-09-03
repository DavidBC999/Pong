from telnetlib import LOGOUT
import pygame
import button
pygame.init()
ballx = 615
bally = 340
ballvelocityx = -2
ballvelocityy = 1
hit = 0
left_score = 0
right_score = 10
scoreFont = pygame.font.SysFont("Times New Roman", 75)
menuFont = pygame.font.SysFont("Times New Roman", 200)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
menuScreen = True

# Show the bases that the players will be moving around
def draw_gamescreen():
    screen.fill("purple")  # Fill the display with a solid color
    screen.blit(base, (base_x,base_y))
    screen.blit(base2, (base2_x,base2_y))
    #screen.blit(stars, (100,0))
    screen.blit(line, (605,10))
    screen.blit(line2, (605,100))
    screen.blit(line3, (605,190))
    screen.blit(line4, (605,280))
    screen.blit(line5, (605,370))
    screen.blit(line6, (605,460))
    screen.blit(line7, (605,550))
    screen.blit(line8, (605,640))
    screen.blit(left_score_label, (200,150))
    screen.blit(right_score_label, (1020,150))
    pygame.draw.circle(screen, "white", (ballx,bally), 20)
    pygame.draw.rect(screen, "black", (0,0,1230,10))
    pygame.draw.rect(screen, "black", (0,670,1230,10))
    pygame.draw.rect(screen,"red",(0,10,10,660))
    pygame.draw.rect(screen,"red",(1220,10,10,660))
def draw_gameoverscreen():
    screen.fill((255,35,50))
    screen.blit(scoreFont.render("Game Over!", 0, (255,255,255)), (435,80))
    screen.blit(scoreFont.render("Winner: "+winner, 0, (255,255,255)),(340,250))
    tryAgainButton = button.Button(560,400,140,60, white, "Home", black)
    tryAgainButton.draw(screen)
   ##pygame.draw.rect(screen, "white", (560,400, 140, 60))
def draw_menuscreen():
    screen.fill((20,150,230))
    screen.blit(scoreFont.render("Welcome to Pong.py", 0, white),(270,80))
    startButton = button.Button(5,230,600,60,white, "                         Start", (20,150,230))
    startButton.draw(screen)
    quitButton = button.Button(610,230,615,60,white,"                         Quit",(20,150,230))
    quitButton.draw(screen)
    screen.blit(logo, (420,300))

def draw_themescreen():
    screen.fill((20,150,230))
    screen.blit(scoreFont.render("Choose a theme", 0, white),(330,80))

pygame.display.set_caption('Pong')
screen = pygame.display.set_mode((1230,680))

base = pygame.image.load("base.jpg")

base2 = pygame.image.load("base2.jpg")

logo = pygame.image.load("logo.jpg")
logo_size = (400, 380)
logo = pygame.transform.scale(logo, logo_size)

#stars = pygame.image.load("stars.jpg")
#star_size = (1000, 540)
#stars = pygame.transform.scale(stars, star_size)

line = pygame.image.load("line.jpg")
line2 = pygame.image.load("line.jpg")
line3 = pygame.image.load("line.jpg")
line4= pygame.image.load("line.jpg")
line5 = pygame.image.load("line.jpg")
line6 = pygame.image.load("line.jpg")
line7 = pygame.image.load("line.jpg")
line8 = pygame.image.load("line.jpg")

clock = pygame.time.Clock()

#screen.fill("purple")  # Fill the display with a solid color

base_x = 30
base_y = 280
base2_x = 1170
base2_y = 280

while True:

    while menuScreen:
        draw_menuscreen()
        clock.tick(60)         # wait until next frame (at 60 FPS)
        pygame.display.flip()  # Refresh on-screen display
    # Process player inputs.
    ballx += ballvelocityx
    bally += ballvelocityy

    if bally >= 650 or bally <= 30:
        ballvelocityy = -ballvelocityy        

    if ballx >= 1220:
        left_score+=1
        ballx = 615
        bally = 340
        hit  = 0
    
    if ballx <= 10:
        right_score+=1
        ballx = 615
        bally = 340
        hit  = 0

    left_score_label = scoreFont.render(str(left_score), 0, (255,255,255))
    right_score_label = scoreFont.render(str(right_score), 0, (255,255,255))

    if left_score == 10:
        while True:
            winner = "Left Side"
            draw_gameoverscreen()
            clock.tick(60)         # wait until next frame (at 60 FPS)
            pygame.display.flip()  # Refresh on-screen display

    if right_score == 10:
        while True:
            winner = "Right Side"
            draw_gameoverscreen()
            clock.tick(60)         # wait until next frame (at 60 FPS)
            pygame.display.flip()  # Refresh on-screen display


    if hit >= 5:
        ballvelocityx += 5
        ballvelocityy += 5
    if hit >= 10:
        ballvelocityx += 0.5
        ballvelocityy += 0.5
    if hit >= 15:
        ballvelocityx += 0.5
        ballvelocityy += 0.5
    if hit >= 20:
        ballvelocityx += 0.5
        ballvelocityy += 0.5
    if hit >= 25:
        ballvelocityx += 0.5
        ballvelocityy += 0.5
    if hit >= 30:
        ballvelocityx += 0.5
        ballvelocityy += 0.5
    if hit >= 35:
        ballvelocityx += 0.5
        ballvelocityy += 0.5
    if hit >= 40:
        ballvelocityx += 0.5
        ballvelocityy += 0.5
    if hit >= 45:
        ballvelocityx += 0.5
        ballvelocityy += 0.5
    if hit >= 50:
        ballvelocityx += 0.5
        ballvelocityy += 0.5
    if hit >= 75:
        ballvelocityx += 2.5
        ballvelocityy += 2.5
    if hit >= 100:
        ballvelocityx += 5
        ballvelocityy += 5

    if ((ballx >= base_x and ballx <= base_x + 60) and (bally >= base_y and bally <= base_y+256)) or ((ballx >= base2_x-20 and ballx <= base2_x + 40) and (bally >= base2_y and bally <= base2_y+256)):
        
        ballvelocityx = -ballvelocityx
        hit += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                base_y -= 50
            if event.key == pygame.K_s:
                base_y += 50

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                base2_y -= 50
            if event.key == pygame.K_DOWN:
                base2_y += 50

    # Do logical updates here.
    # ...

    
    # Sprite movement
    print(base_x, base_y)
    print(base2_x,base2_y)
    #screen.blit(base, (base_x,base_y))
    draw_gamescreen()
    clock.tick(60)         # wait until next frame (at 60 FPS)
    pygame.display.flip()  # Refresh on-screen display
