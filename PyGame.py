
 #Import Libraries
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define block sizes
BLOCK_SIZE = 20

# Define the snake
snake_speed = 10
snake_x = SCREEN_WIDTH / 2
snake_y = SCREEN_HEIGHT / 2
snake_x_change = 0
snake_y_change = 0
snake_body = []
snake_length = 1

# Define the food
food_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
food_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

# Define the obstacle
obstacle_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
obstacle_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

# Define the score
score = 0

# Function to display score
def display_score():
    font = pygame.font.SysFont(None, 25)
    score_display = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_display, (10, 10))

# Function to draw snake
def draw_snake(snake_body):
    for part in snake_body:
        pygame.draw.rect(screen, GREEN, [part[0], part[1], BLOCK_SIZE, BLOCK_SIZE])

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and snake_x_change == 0:
                snake_x_change = -BLOCK_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_d and snake_x_change == 0:
                snake_x_change = BLOCK_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_w and snake_y_change == 0:
                snake_y_change = -BLOCK_SIZE
                snake_x_change = 0
            elif event.key == pygame.K_s and snake_y_change == 0:
                snake_y_change = BLOCK_SIZE
                snake_x_change = 0

    # Move the snake
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for wall collision
    if snake_x < 0 or snake_x >= SCREEN_WIDTH or snake_y < 0 or snake_y >= SCREEN_HEIGHT:
        screen.fill(RED)
        font = pygame.font.SysFont(None, 50)
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) // 2, (SCREEN_HEIGHT - game_over_text.get_height()) // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds
        snake_x = SCREEN_WIDTH / 2
        snake_y = SCREEN_HEIGHT / 2
        snake_body = []
        snake_length = 1
        snake_x_change = 0
        snake_y_change = 0
        food_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        obstacle_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        obstacle_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        score = 0
        continue

    # Check for food collision
    if snake_x == food_x and snake_y == food_y:
        score += 1
        snake_length += 1
        food_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

    # Check for obstacle collision
    if snake_x == obstacle_x and snake_y == obstacle_y:
        score += 1
        snake_length += 1
        obstacle_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        obstacle_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

    # Update snake body
    snake_head = [snake_x, snake_y]
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Check for self-collision
    for part in snake_body[:-1]:
        if part == snake_head:
            running = False

    # Clear the screen
    screen.fill(RED)

    # Draw food
    pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

    # Draw obstacle
    pygame.draw.rect(screen, BLUE, [obstacle_x, obstacle_y, BLOCK_SIZE, BLOCK_SIZE])

    # Draw snake
    draw_snake(snake_body)

    # Display score
    display_score()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(snake_speed)

    # Check for winning condition
    if score >= 1000:
        running = False

# Quit Pygame
pygame.quit()
sys.exit()
