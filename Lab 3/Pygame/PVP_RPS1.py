import random
import time
import paho.mqtt.client as mqtt
import numpy as np
import pygame

#=========================Communication---------------------------------------------------------------------------
def on_connect(client, userdata, flags, rc):
    client.subscribe("result",1)
    client.subscribe("player1",1)
    client.subscribe("player2",1)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")
        
resultmsg = ""
player1msg = ""
player2msg = ""
def on_message(client, userdata, message):   
    global player1msg 
    global player2msg 
    global resultmsg 
    if(message.topic == "player1"):
        player1msg = message.payload.decode()
    elif(message.topic == "player2"):
        player2msg = message.payload.decode()
    elif(message.topic == "result"):
        resultmsg = message.payload.decode()

#----------------------------------------------------------Front-end (Game Interface) --------------------------------------------------
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_q,
    K_w,
    K_e,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect_async("mqtt.eclipseprojects.io")

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
pygame.display.set_caption('Rock,Paper,Scissor')
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

rock = Rock()
paper = Paper()
scissor = Scissor()

client.loop_start()

screen1 = False
screen2 = False
screen3 = False
screen4 = False
screen5 = False

again = True
running = True
while running:
    #Update your screen display
    if(player1msg == "" and player2msg == "" and again == True):
        screen1 = True
        screen2 = False
        screen3 = False
        screen4 = False
        screen5 = False
    elif(player1msg != "" and player2msg == ""):
        screen1 = False
        if(count % 3 == 1):
            screen2 = True
            screen3 = False
            screen4 = False
        elif(count % 3 == 2):
            screen2 = False
            screen3 = True
            screen4 = False
        elif(count % 3 == 0):
            screen2 = False
            screen3 = False
            screen4 = True
        screen5 = False
        count = count + 1
    elif(player1msg != "" and player2msg != "" and resultmsg != ""):
        screen1 = False
        screen2 = False
        screen3 = False
        screen4 = False
        screen5 = True
    
    pressed_keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        #Key_click
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif (event.key == K_q and screen1 == True):
                client.publish("player1","rock",1)
            elif (event.key == K_e and screen1 == True):
                client.publish("player1","paper",1)
            elif (event.key == K_w and screen1 == True):
                client.publish("player1","scissor",1)
            elif (event.key == K_SPACE and screen5 == True):
                screen1 = True
        #Mouse_click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(280 <= mouse[0] <= 330 and 500<=mouse[1] <= 550 and screen1 == True):
                client.publish("player1","rock",1)
            elif(380 <= mouse[0] <= 430 and 500<=mouse[1] <= 550 and screen1 == True):
                client.publish("player1","paper",1)
            elif(480 <= mouse[0] <= 530 and 500 <=mouse[1] <= 550 and screen1 == True):
                client.publish("player1","scissor",1)
            elif(350 <= mouse[0] <= 450 and 550 <=mouse[1] <= 600 and screen5 == True):
                screen1 = True
        elif event.type == QUIT:
                running = False

    screen.fill((66, 245, 90))
    #show your sprite in "screen" 
    if(screen1 == True):
        count = 1
        screen.blit(rock.surf,(280,500))
        screen.blit(paper.surf,(380,500))
        screen.blit(scissor.surf,(480,500))
        text_surface = font.render("rock,paper,scissor", True, (0,0,0))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-250))
        screen.blit(text_surface,text_rect)
        instr_surface1 = font.render("instruction:", True, (255,255,255))
        screen.blit(instr_surface1,(330,100))
        instr_surface2 = font.render("Click the icon or type in your gesture", True, (255,255,255))
        screen.blit(instr_surface2,(210,130))
        instr_surface3 = font.render("A=Rock, S=Paper, D=Scissor", True, (255,255,255))
        screen.blit(instr_surface3,(250,160))
    elif(screen2 == True):
        again = False
        text_surface = font.render("rock,paper,scissor", True, (0,0,0))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-250))
        screen.blit(text_surface,text_rect)
        wait_surface = font.render("Waiting other players responses..", True, (0,0,0))
        screen.blit(wait_surface,(320,450))
    elif(screen3 == True):
        again = False
        text_surface = font.render("rock,paper,scissor", True, (0,0,0))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-250))
        screen.blit(text_surface,text_rect)
        wait_surface = font.render("Waiting other players responses....", True, (0,0,0))
        screen.blit(wait_surface,(320,450))
    elif(screen4 == True):
        again = False
        text_surface = font.render("rock,paper,scissor", True, (0,0,0))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-250))
        screen.blit(text_surface,text_rect)
        wait_surface = font.render("Waiting other players responses......", True, (0,0,0))
        screen.blit(wait_surface,(320,450))
    elif(screen5 == True):
        again = False
        player1msg = ""
        player2msg = ""
        text_surface = font.render("rock,paper,scissor", True, (0,0,0))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-250))
        screen.blit(text_surface,text_rect)
        again_surface = font.render("again", True, (0,0,0))
        guess_surface = font.render(resultmsg, True, (0,0,0))
        guess_rect = guess_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(guess_surface,guess_rect)
        screen.blit(again_surface,(370,550))

    pygame.display.flip()
    clock.tick(5)

client.loop_stop()
client.disconnect()