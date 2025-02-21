import pygame
import time

pygame.init()

# Skærm opsætning
WIDTH, HEIGHT = 1500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2 Player Game")

# Farver
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # Blå spiller
RED = (255, 0, 0)   # Rød spiller
BLACK = (0, 0, 0)
BULLET_COLOR = (0, 0, 0)  # Kugler er sorte

# Spillerens startpositioner
player1_x, player1_y = WIDTH - 150, HEIGHT // 2  # Rød spiller (højre side)
player2_x, player2_y = 100, HEIGHT // 2  # Blå spiller (venstre side)


# Bevægelseshastighed
player_speed = 5
bullet_speed = 10

# Lister til kugler
player1_bullets = []  # Blå spillers skud
player2_bullets = []  # Rød spillers skud

# Font til tekst
font = pygame.font.SysFont("Arial", 50)

running = True

while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Spillere skyder kugler
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Blå spiller skyder
                player1_bullets.append([player1_x + 50, player1_y + 25])  # Kuglen starter ved spilleren
            if event.key == pygame.K_SPACE:  # Rød spiller skyder
                player2_bullets.append([player2_x, player2_y + 25])  # Kuglen starter ved spilleren

    # **Blå spiller (Piletaster)**
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player1_x -= player_speed
    if keys[pygame.K_RIGHT]: player1_x += player_speed
    if keys[pygame.K_UP]: player1_y -= player_speed
    if keys[pygame.K_DOWN]: player1_y += player_speed

    # **Rød spiller (WASD)**
    if keys[pygame.K_a]: player2_x -= player_speed
    if keys[pygame.K_d]: player2_x += player_speed
    if keys[pygame.K_w]: player2_y -= player_speed
    if keys[pygame.K_s]: player2_y += player_speed

    # 🚀 Opdater kugler
    for bullet in player1_bullets:
        bullet[0] -= bullet_speed  # Skyd mod højre
        if bullet[0] > WIDTH:  # Fjern kugler uden for skærmen
            player1_bullets.remove(bullet)

    for bullet in player2_bullets:
        bullet[0] += bullet_speed  # Skyd mod venstre
        if bullet[0] < 0:  # Fjern kugler uden for skærmen
            player2_bullets.remove(bullet)



    # Tegn alt på skærmen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player1_x, player1_y, 50, 50))  # Blå spiller
    pygame.draw.rect(screen, RED, (player2_x, player2_y, 50, 50))   # Rød spiller

    # Tegn kugler
    for bullet in player1_bullets:
        pygame.draw.rect(screen, BULLET_COLOR, (bullet[0], bullet[1], 10, 5))

    for bullet in player2_bullets:
        pygame.draw.rect(screen, BULLET_COLOR, (bullet[0], bullet[1], 10, 5))

    pygame.display.update()  # Opdater skærmen

screen.fill(WHITE)
pygame.display.update()
pygame.time.delay(5000)

pygame.quit()
