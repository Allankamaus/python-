import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Window")

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with white
    screen.fill(WHITE)

    # Draw a red rectangle (x, y, width, height)
    pygame.draw.rect(screen, RED, (100, 100, 200, 150))

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()