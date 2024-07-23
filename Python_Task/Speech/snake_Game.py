import pygame
import time
import random

pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
SNAKE_SPEED = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initial position
snake = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
snake_direction = (0, -GRID_SIZE)

# Food initial position
food = (random.randint(0, WINDOW_WIDTH // GRID_SIZE - 1) * GRID_SIZE,
        random.randint(0, WINDOW_HEIGHT // GRID_SIZE - 1) * GRID_SIZE)

clock = pygame.time.Clock()

def draw_snake():
    for segment in snake:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

def draw_food():
    pygame.draw.rect(window, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

def move_snake():
    global food

    head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, head)

    if snake[0] == food:
        food = (random.randint(0, WINDOW_WIDTH // GRID_SIZE - 1) * GRID_SIZE,
                random.randint(0, WINDOW_HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
    else:
        snake.pop()

def game_over():
    font = pygame.font.SysFont(None, 70)
    text = font.render("Game Over", True, RED)
    window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_direction = (-GRID_SIZE, 0)
    elif keys[pygame.K_RIGHT]:
        snake_direction = (GRID_SIZE, 0)
    elif keys[pygame.K_UP]:
        snake_direction = (0, -GRID_SIZE)
    elif keys[pygame.K_DOWN]:
        snake_direction = (0, GRID_SIZE)

    move_snake()

    window.fill(BLACK)
    draw_snake()
    draw_food()
    pygame.display.update()

    if (snake[0][0] < 0 or snake[0][0] >= WINDOW_WIDTH or
        snake[0][1] < 0 or snake[0][1] >= WINDOW_HEIGHT or
        snake[0] in snake[1:]):
        game_over()

    clock.tick(SNAKE_SPEED)
