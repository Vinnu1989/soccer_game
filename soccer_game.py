import pygame
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 660
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Soccer Game")

FPS = 20
clock = pygame.time.Clock()

player1_color = (0, 0, 255)
player1_x, player1_y = 300, 300
player1a_x, player1a_y = 300, 350
player1b_x, player1b_y = 337.5, 312.5
player1c_x, player1c_y = 287.5, 312.5

player12_width, player12_height = 50, 25

ball_color = (255, 255, 255)
ball_x, ball_y = WINDOW_WIDTH//2, WINDOW_HEIGHT//2
ball_width, ball_height = 50, 50

running = True
while running:
    display.fill("light green")
    player_1 = pygame.draw.rect(display, player1_color, (player1_x, player1_y, player12_width, player12_height))
    player_1x = pygame.draw.rect(display, player1_color, (player1a_x, player1a_y, 50, 25))
    player_1y = pygame.draw.rect(display, player1_color, (player1b_x, player1b_y, 25, 50))
    player_1z = pygame.draw.rect(display, player1_color, (player1c_x, player1c_y, 25, 50))
    B_all = pygame.draw.rect(display, ball_color, (ball_x, ball_y, ball_width, ball_height))
    wall_1 = pygame.draw.rect(display, "dark green", (0, 0, 1280, 20))
    wall_2 = pygame.draw.rect(display, "dark green", (0, 640, 1280, 20))
    wall_3 = pygame.draw.rect(display, "dark green", (0, 0, 20, 660))
    wall_4 = pygame.draw.rect(display, "dark green", (1260, 0, 20, 660))
    G_oal = pygame.draw.rect(display, (255, 255, 255), (1230, 230, 30, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1_x -= 20
            if event.key == pygame.K_RIGHT:
                player1_x += 20
            if event.key == pygame.K_UP:
                player1_y -= 20
            if event.key == pygame.K_DOWN:
                player1_y += 20

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1a_x -= 20
            if event.key == pygame.K_RIGHT:
                player1a_x += 20
            if event.key == pygame.K_UP:
                player1a_y -= 20
            if event.key == pygame.K_DOWN:
                player1a_y += 20

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1b_x -= 20
            if event.key == pygame.K_RIGHT:
                player1b_x += 20
            if event.key == pygame.K_UP:
                player1b_y -= 20
            if event.key == pygame.K_DOWN:
                player1b_y += 20

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1c_x -= 20
            if event.key == pygame.K_RIGHT:
                player1c_x += 20
            if event.key == pygame.K_UP:
                player1c_y -= 20
            if event.key == pygame.K_DOWN:
                player1c_y += 20

    if player_1.colliderect(B_all):
         ball_y -=50
    if player_1x.colliderect(B_all):
         ball_y +=50
    if player_1y.colliderect(B_all):
         ball_x +=50
    if player_1z.colliderect(B_all):
         ball_x -=50
    if B_all.colliderect(wall_1):
         ball_y +=100
    if B_all.colliderect(wall_2):
         ball_y -=100
    if B_all.colliderect(wall_3):
         ball_x +=100
    if B_all.colliderect(wall_4):
         ball_x -=100
    if B_all.colliderect(G_oal):
        pygame.QUIT

    pygame.display.flip()
    clock.tick(FPS)
pygame.QUIT
