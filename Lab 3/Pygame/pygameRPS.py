# Import the pygame module
import pygame
# Import random for random numbers
import random
import time

#----------------------------------------------------------Back-end (Program) ------------------------------------------------------------
def RPS(inputRPC):
    output = ["rock","paper","scissor"]
    outputRPC = random.choice(output)
    if(outputRPC == inputRPC):
        result = "no winner"
    elif(outputRPC == "rock" and inputRPC == "paper"):
        result = "you win"
    elif(outputRPC == "rock" and inputRPC == "scissor"):
        result = "you lose"
    elif(outputRPC == "paper" and inputRPC == "scissor"):
        result = "you win"
    elif(outputRPC == "paper" and inputRPC == "rock"):
        result = "you lose"
    elif(outputRPC == "scissor" and inputRPC == "rock"):
        result = "you win"
    elif(outputRPC == "scissor" and inputRPC == "paper"):
        result = "you lose"
    else:
        result = "invalid input"

    return result
#----------------------------------------------------------Front-end (Game Interface) --------------------------------------------------
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_e,
    K_q,
    K_w,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Define Sprites
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super(Rock,self).__init__()
        self.surf = pygame.Surface((70,20))                  #size of your sprite
        self.surf.fill((255,255,255))                        #color of your sprite
        self.rect = self.surf.get_rect()                     #get your coordinate as a rectangular

class Paper(pygame.sprite.Sprite):
    def __init__(self):
        super(Paper,self).__init__()
        self.surf = pygame.Surface((70,20))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

class Scissor(pygame.sprite.Sprite):
    def __init__(self):
        super(Scissor,self).__init__()
        self.surf = pygame.Surface((70,20))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

def display_text(text,duration,pt):
    ct = pygame.time.get_ticks()
    text_surface = font.render(text, True, (0,0,0))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 250))
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    if(ct - pt > duration):
        screen.fill((135, 206, 250))
        screen.blit(rock.surf,(280,500))
        screen.blit(paper.surf,(380,500))
        screen.blit(scissor.surf,(480,500))

    pygame.display.update(text_rect)
    
#Main Operation
pygame.init()
past_time = pygame.time.get_ticks()
pygame.display.set_caption('Rock,Paper,Scissor')
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
rock = Rock()
paper = Paper()
scissor = Scissor()

running = True
while running:
    #Update your screen display
    text_surface = font.render("rock,paper,scissor", True, (0,0,0))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-250))
    guess_surface = font.render("", True, (0,0,0))
    guess_rect = guess_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))    
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_q:
                result = RPS("rock")
                guess_surface = font.render(result, True, (0,0,0))
                guess_rect = guess_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))    
            elif event.key == K_w:
                result = RPS("paper")
                guess_surface = font.render(result, True, (0,0,0))
                guess_rect = guess_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))    
            elif event.key == K_e:
                result = RPS("scissor")
                guess_surface = font.render(result, True, (0,0,0))
                guess_rect = guess_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))    
        elif event.type == QUIT:
                running = False

    screen.fill((135, 206, 250))

    #show your sprite in "screen" 
    screen.blit(rock.surf,(280,500))
    screen.blit(paper.surf,(380,500))
    screen.blit(scissor.surf,(480,500))
    screen.blit(text_surface,text_rect)
    screen.blit(guess_surface,guess_rect)
    pygame.display.flip()
    clock.tick(60)
