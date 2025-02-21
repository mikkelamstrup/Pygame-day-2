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

# Spillerens startpositioner
player1_x, player1_y = 100, HEIGHT // 2  # Blå spiller (venstre side)
player2_x, player2_y = WIDTH - 150, HEIGHT // 2  # Rød spiller (højre side)

# Bevægelseshastighed
player_speed = 5

# Font til tekst
font = pygame.font.SysFont("Arial", 50)

# Timer starter
timeStart = time.time()

running = True
winner = None  # Ingen vinder i starten
elapsedTime = 0  # Gemmer vinderens tid

while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spilleren kan bevæge sig
    keys = pygame.key.get_pressed()

    # 🎮 **Blå spiller (Piletaster)**
    if keys[pygame.K_LEFT]: player1_x -= player_speed
    if keys[pygame.K_RIGHT]: player1_x += player_speed
    if keys[pygame.K_UP]: player1_y -= player_speed
    if keys[pygame.K_DOWN]: player1_y += player_speed

    # 🎮 **Rød spiller (WASD)**
    if keys[pygame.K_a]: player2_x -= player_speed
    if keys[pygame.K_d]: player2_x += player_speed
    if keys[pygame.K_w]: player2_y -= player_speed
    if keys[pygame.K_s]: player2_y += player_speed


    # 🎨 Tegn alt på skærmen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player1_x, player1_y, 50, 50))  # Blå spiller
    pygame.draw.rect(screen, RED, (player2_x, player2_y, 50, 50))   # Rød spiller
    pygame.display.update()  # Opdater skærmen

pygame.quit()
