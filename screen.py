import pygame
# Initialize Pygame
pygame.init()
# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game Screen")
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with a color
    screen.fill((135, 206, 235))  # Sky blue
    
    # Update the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()