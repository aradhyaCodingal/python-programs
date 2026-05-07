import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game with Elements")
# Set up font for text
font = pygame.font.Font(None, 74)
text = font.render("Welcome to My Game!", True, (255, 255, 255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((50, 50, 100))  # Dark blue background
    
    # Draw a rectangle
    pygame.draw.rect(screen, (255, 100, 100), (300, 250, 200, 100))
    
    # Draw text
    screen.blit(text, (150, 100))
    
    pygame.display.flip()
pygame.quit()