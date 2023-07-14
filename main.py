import pygame
pygame.init()
ballx = 615
bally = 340
ballvelocityx = 2
ballvelocityy = 2
hit = 0
# Show the bases that the players will be moving around
def draw_screen():
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
    pygame.draw.circle(screen, "white", (ballx,bally), 20)
    pygame.draw.rect(screen, "black", (0,0,1230,10))
    pygame.draw.rect(screen, "black", (0,670,1230,10))
    pygame.draw.rect(screen,"red",(0,10,10,660))
    pygame.draw.rect(screen,"red",(1220,10,10,660))

pygame.display.set_caption('Pong')
screen = pygame.display.set_mode((1230,680))

base = pygame.image.load("base.jpg")

base2 = pygame.image.load("base2.jpg")


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

    # Process player inputs.
    ballx += ballvelocityx
    bally += ballvelocityy

    if bally == 650 or bally == 30:
        ballvelocityy = -ballvelocityy

    if ballx == 1220 or ballx == 10:
        ballx = 615
        bally = 340
        hit  = 0

    
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

    if (ballx == base_x + 60 and (bally >= base_y and bally <= base_y+256)) or (ballx == base2_x-20 and (bally >= base2_y and bally <= base2_y+256)):
        
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
    draw_screen()
    clock.tick(60)         # wait until next frame (at 60 FPS)
    pygame.display.flip()  # Refresh on-screen display
