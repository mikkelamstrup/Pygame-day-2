import pygame
import time
import random

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
GREEN = (0, 255, 0)  # Power-up farve
BULLET_COLOR = (0, 0, 0)  # Kugler er sorte

# Spillerens startpositioner
player1_x, player1_y = WIDTH - 150, HEIGHT // 2  # Rød spiller (højre side)
player2_x, player2_y = 100, HEIGHT // 2  # Blå spiller (venstre side)

# Bevægelseshastighed
player_speed = 5
bullet_speed = 10
boost_speed = 8  # Hurtigere hastighed efter power-up

# Lister til kugler
player1_bullets = []  # Blå spillers skud
player2_bullets = []  # Rød spillers skud

# Power-up placering
powerup_x = random.randint(200, WIDTH - 200)
powerup_y = random.randint(100, HEIGHT - 100)
powerup_active = True  # Power-up findes i starten

# Font til tekst
font = pygame.font.SysFont("Arial", 50)

running = True
winner = None  # Ingen vinder i starten
player1_boost = False
player2_boost = False
boost_start_time = 0

while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Spillere skyder kugler
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Blå spiller skyder
                player1_bullets.append([player1_x + 50, player1_y + 25])  
            if event.key == pygame.K_SPACE:  # Rød spiller skyder
                player2_bullets.append([player2_x, player2_y + 25])  

    # **Blå spiller (Piletaster)**
    keys = pygame.key.get_pressed()
    speed1 = boost_speed if player1_boost else player_speed  # Hurtigere hvis power-up aktiv
    if keys[pygame.K_LEFT]: player1_x -= speed1
    if keys[pygame.K_RIGHT]: player1_x += speed1
    if keys[pygame.K_UP]: player1_y -= speed1
    if keys[pygame.K_DOWN]: player1_y += speed1

    # **Rød spiller (WASD)**
    speed2 = boost_speed if player2_boost else player_speed
    if keys[pygame.K_a]: player2_x -= speed2
    if keys[pygame.K_d]: player2_x += speed2
    if keys[pygame.K_w]: player2_y -= speed2
    if keys[pygame.K_s]: player2_y += speed2

    # Opdater kugler
    for bullet in player1_bullets:
        bullet[0] -= bullet_speed  
        if bullet[0] < 0:  
            player1_bullets.remove(bullet)

    for bullet in player2_bullets:
        bullet[0] += bullet_speed  
        if bullet[0] > WIDTH:  
            player2_bullets.remove(bullet)

    # Tjek for kollision mellem kugler og modstandere
    for bullet in player1_bullets:
        if player2_x < bullet[0] < player2_x + 50 and player2_y < bullet[1] < player2_y + 50:
            winner = "BLUE"
            running = False

    for bullet in player2_bullets:
        if player1_x < bullet[0] < player1_x + 50 and player1_y < bullet[1] < player1_y + 50:
            winner = "RED"
            running = False

    # Tjek for power-up kollision
    if powerup_active and player1_x < powerup_x < player1_x + 50 and player1_y < powerup_y < player1_y + 50:
        player1_boost = True
        powerup_active = False  # Power-up forsvinder
        boost_start_time = time.time()

    if powerup_active and player2_x < powerup_x < player2_x + 50 and player2_y < powerup_y < player2_y + 50:
        player2_boost = True
        powerup_active = False
        boost_start_time = time.time()

    # Fjern power-up boost efter 5 sekunder
    if player1_boost or player2_boost:
        if time.time() - boost_start_time > 5:  # Boost varer 5 sekunder
            player1_boost = False
            player2_boost = False

    # Tegn alt på skærmen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player1_x, player1_y, 50, 50))  
    pygame.draw.rect(screen, RED, (player2_x, player2_y, 50, 50))   

    # Tegn kugler
    for bullet in player1_bullets:
        pygame.draw.rect(screen, BULLET_COLOR, (bullet[0], bullet[1], 10, 5))

    for bullet in player2_bullets:
        pygame.draw.rect(screen, BULLET_COLOR, (bullet[0], bullet[1], 10, 5))

    # Tegn power-up, hvis den er aktiv
    if powerup_active:
        pygame.draw.rect(screen, GREEN, (powerup_x, powerup_y, 30, 30))

    pygame.display.update()  

# Når spillet slutter, vis vinderen
screen.fill(WHITE)
win_text = font.render(f"{winner} WINS!", True, BLACK)
screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
pygame.display.update()
pygame.time.delay(5000)

pygame.quit()
