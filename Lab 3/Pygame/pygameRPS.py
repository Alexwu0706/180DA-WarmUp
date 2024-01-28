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
    K_z,
    K_x,
    K_c,
    K_SPACE,
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
        self.surf = pygame.image.load('rock.png')                           #size of your sprite
        self.surf = pygame.transform.scale(self.surf, (50,50))
        #self.surf.set_colorkey((255, 255, 255), RLEACCEL)                     #color of your sprite
        self.rect = self.surf.get_rect()                     #get your coordinate as a rectangular

class Paper(pygame.sprite.Sprite):
    def __init__(self):
        super(Paper,self).__init__()
        self.surf = pygame.image.load('paper.png')                           #size of your sprite
        self.surf = pygame.transform.scale(self.surf, (50,50))
        #self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

class Scissor(pygame.sprite.Sprite):
    def __init__(self):
        super(Scissor,self).__init__()
        self.surf = pygame.image.load('scissor.png')                           #size of your sprite
        self.surf = pygame.transform.scale(self.surf, (50,50))
        #self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

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

#Loop Process
running = True
again = True
while running:
    #Update your screen display
    
    text_surface = font.render("rock,paper,scissor", True, (0,0,0))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-250))

    pressed_keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        #Key_click
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif (event.key == K_z and again == True):
                result = RPS("rock")
                guess_surface = font.render(result, True, (0,0,0))
                guess_rect = guess_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                again = False
            elif (event.key == K_x and again == True):
                result = RPS("paper")
                guess_surface = font.render(result, True, (0,0,0))
                guess_rect = guess_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                again = False   
            elif (event.key == K_c and again == True):
                result = RPS("scissor")
                guess_surface = font.render(result, True, (0,0,0))
                guess_rect = guess_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)) 
                again = False
            elif (event.key == K_SPACE):
                again = True
        #Mouse_click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(280 <= mouse[0] <= 330 and 500<=mouse[1] <= 550):
                result = RPS("rock")
                guess_surface = font.render(result, True, (0,0,0))
                guess_rect = guess_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                again = False
            elif(380 <= mouse[0] <= 430 and 500<=mouse[1] <= 550):
                result = RPS("paper")
                guess_surface = font.render(result, True, (0,0,0))
                guess_rect = guess_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                again = False
            elif(480 <= mouse[0] <= 530 and 500 <=mouse[1] <= 550):
                result = RPS("scissor")
                guess_surface = font.render(result, True, (0,0,0))
                guess_rect = guess_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                again = False
            elif(350 <= mouse[0] <= 450 and 550 <=mouse[1] <= 600):
                again = True
        elif event.type == QUIT:
                running = False

    screen.fill((135, 206, 250))
    #show your sprite in "screen" 
    if(again == True):
        screen.blit(rock.surf,(280,500))
        screen.blit(paper.surf,(380,500))
        screen.blit(scissor.surf,(480,500))
        screen.blit(text_surface,text_rect)
    else:
        again_surface = font.render("again", True, (0,0,0))
        screen.blit(guess_surface,guess_rect)
        screen.blit(again_surface,(350,550))

    pygame.display.flip()
    clock.tick(60)
