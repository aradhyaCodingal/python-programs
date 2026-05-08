import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add Sprites Assignment")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        # Create the rectangular look of the sprite
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def update(self, keys):
        # Movement controls for the player sprite
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

# Create sprite groups
all_sprites = pygame.sprite.Group()

# Create two rectangular sprites
player = Block(BLUE, 50, 50, 100, 100)  # The controllable sprite
static_block = Block(RED, 50, 50, 400, 300) # The static sprite

all_sprites.add(player)
all_sprites.add(static_block)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys and update the player sprite
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Drawing
    screen.fill(WHITE) # Background color
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60) # Limit to 60 frames per second

pygame.quit()