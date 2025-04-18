import pygame
import time
import random

pygame.init()

# Skærm opsætning
WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2 Player Game")

# Farver
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
BULLET_COLOR = (0, 0, 0)

# Spillerens startpositioner
def reset_positions():
    global player1_x, player1_y, player2_x, player2_y, powerup_x, powerup_y, powerup_active, bigBullet_x, bigBullet_y, bigBullet_active
    player1_x, player1_y = WIDTH - 150, HEIGHT // 2
    player2_x, player2_y = 100, HEIGHT // 2
    
    powerup_x = random.randint(200, WIDTH - 200)
    powerup_y = random.randint(100, HEIGHT - 100)
    powerup_active = True
    
    bigBullet_x = random.randint(200, WIDTH - 200)
    bigBullet_y = random.randint(100, HEIGHT - 100)
    bigBullet_active = True

reset_positions()

# Bevægelseshastighed
player_speed = 5
bullet_speed = 10
boost_speed = 8

# Lister til kugler
player1_bullets = []
player2_bullets = []

# Power-ups
powerup_active = True
bigBullet_active = True
boost_start_time = 0
bigBullet_start_time = 0
player1_boost = False
player2_boost = False
player1_bigBullet = False
player2_bigBullet = False

# Point system
player1_score = 0
player2_score = 0
winning_score = 5

# Font
font = pygame.font.SysFont("Arial", 50)

running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                size = 20 if player1_bigBullet else 10
                player1_bullets.append([player1_x + 50, player1_y + 25, size, size])
            if event.key == pygame.K_SPACE:
                size = 20 if player2_bigBullet else 10
                player2_bullets.append([player2_x, player2_y + 25, size, size])

    keys = pygame.key.get_pressed()
    speed1 = boost_speed if player1_boost else player_speed
    if keys[pygame.K_LEFT]: player1_x -= speed1
    if keys[pygame.K_RIGHT]: player1_x += speed1
    if keys[pygame.K_UP]: player1_y -= speed1
    if keys[pygame.K_DOWN]: player1_y += speed1
    
    speed2 = boost_speed if player2_boost else player_speed
    if keys[pygame.K_a]: player2_x -= speed2
    if keys[pygame.K_d]: player2_x += speed2
    if keys[pygame.K_w]: player2_y -= speed2
    if keys[pygame.K_s]: player2_y += speed2
    
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
            player1_score += 1  # Blå spiller får 1 point
            if player1_score == winning_score:  # Blå vinder spillet
                winner = "BLUE"
                screen.fill(WHITE)
                win_text = font.render(f"{winner} WINS!", True, BLACK)
                screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
                pygame.display.update()
                pygame.time.delay(5000)  # Vis vinder i 5 sekunder
                player1_score = 0  # Reset score
                player2_score = 0
            reset_positions()
            player1_bullets.clear()
            player2_bullets.clear()

    for bullet in player2_bullets:
        if player1_x < bullet[0] < player1_x + 50 and player1_y < bullet[1] < player1_y + 50:
            player2_score += 1  # Rød spiller får 1 point
            if player2_score == winning_score:  # Rød vinder spillet
                winner = "RED"
                screen.fill(WHITE)
                win_text = font.render(f"{winner} WINS!", True, BLACK)
                screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
                pygame.display.update()
                pygame.time.delay(5000)  # Vis vinder i 5 sekunder
                player1_score = 0  # Reset score
                player2_score = 0
            reset_positions()
            player1_bullets.clear()
            player2_bullets.clear()
    
    if powerup_active and player1_x < powerup_x < player1_x + 50 and player1_y < powerup_y < player1_y + 50:
        player1_boost = True
        powerup_active = False
        boost_start_time = time.time()
    
    if powerup_active and player2_x < powerup_x < player2_x + 50 and player2_y < powerup_y < player2_y + 50:
        player2_boost = True
        powerup_active = False
        boost_start_time = time.time()
    
    if bigBullet_active and player1_x < bigBullet_x < player1_x + 50 and player1_y < bigBullet_y < player1_y + 50:
        player1_bigBullet = True
        bigBullet_active = False
        bigBullet_start_time = time.time()
    
    if bigBullet_active and player2_x < bigBullet_x < player2_x + 50 and player2_y < bigBullet_y < player2_y + 50:
        player2_bigBullet = True
        bigBullet_active = False
        bigBullet_start_time = time.time()
    
    if player1_bigBullet or player2_bigBullet:
        if time.time() - bigBullet_start_time > 5:
            player1_bigBullet = False
            player2_bigBullet = False
    
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player1_x, player1_y, 50, 50))  
    pygame.draw.rect(screen, RED, (player2_x, player2_y, 50, 50))   
    
    for bullet in player1_bullets:
        pygame.draw.rect(screen, BULLET_COLOR, (bullet[0], bullet[1], bullet[2], bullet[3]))
    
    for bullet in player2_bullets:
        pygame.draw.rect(screen, BULLET_COLOR, (bullet[0], bullet[1], bullet[2], bullet[3]))
    
    if powerup_active:
        pygame.draw.rect(screen, GREEN, (powerup_x, powerup_y, 30, 30))
    
    if bigBullet_active:
        pygame.draw.rect(screen, PURPLE, (bigBullet_x, bigBullet_y, 30, 30))
    
    score_text = font.render(f"BLUE: {player1_score}   RED: {player2_score}", True, BLACK)
    screen.blit(score_text, (WIDTH // 2 - 150, 20))
    
    pygame.display.update()

pygame.quit()
