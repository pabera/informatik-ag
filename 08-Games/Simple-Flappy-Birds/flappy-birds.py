import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Bird properties
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 20
bird_velocity = 0
gravity = 0.5
jump_strength = -10

# Pipe properties
pipe_width = 50
pipe_gap = 200
pipe_x = WIDTH
pipe_speed = 3
pipe_list = []

# Game variables
score = 0
passed_pipes = []  # To keep track of pipes that have been passed
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()
running = True

def create_pipe():
    pipe_height = random.randint(100, HEIGHT - 100 - pipe_gap)
    bottom_pipe = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT - pipe_height - pipe_gap)
    top_pipe = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
    return bottom_pipe, top_pipe

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

def move_pipes(pipes):
    for pipe in pipes:
        pipe.x -= pipe_speed
    return [pipe for pipe in pipes if pipe.right > 0]

def check_collision(pipes):
    bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius * 2, bird_radius * 2)
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    if bird_y + bird_radius > HEIGHT or bird_y - bird_radius < 0:
        return True
    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    # Update bird position
    bird_velocity += gravity
    bird_y += bird_velocity

    # Create and move pipes
    if len(pipe_list) == 0 or pipe_list[-1].right < WIDTH - 200:
        pipe_list.extend(create_pipe())
    pipe_list = move_pipes(pipe_list)

    # Check for collisions
    if check_collision(pipe_list):
        running = False

    # Update score
    for i in range(0, len(pipe_list), 2):
        pipe = pipe_list[i]
        if pipe.right < bird_x and pipe not in passed_pipes:
            score += 1
            passed_pipes.append(pipe)

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (int(bird_x), int(bird_y)), bird_radius)
    draw_pipes(pipe_list)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()