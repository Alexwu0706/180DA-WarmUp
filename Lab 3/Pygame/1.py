import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Display Words for a Short Time")

# Set up font
font = pygame.font.Font(None, 36)

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Function to display text
def display_text(text, duration):
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(text_surface, text_rect)
    if((pygame.time.get_ticks() - past_time > duration)):
        screen.fill((0,0,0))
    pygame.display.flip()

# Main game loop
    
past_time = pygame.time.get_ticks()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Display text for 2 seconds
    display_text("hello,word",2000)

    # Update the display
    pygame.display.flip()

