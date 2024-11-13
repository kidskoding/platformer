import pygame

# Intialize the pygame module
pygame.init()

# Create a 800x800 resolution game window display and set the title of the game window
display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Platformer")

# Load the background images
sun = pygame.image.load("img/sun.png")
bg = pygame.image.load("img/sky.png")

running = True
while running:
    # Add the background images to the display
    display.blit(bg, (0, 0))
    display.blit(sun, (100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()