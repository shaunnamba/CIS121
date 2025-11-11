import copy
import random
import pygame

cards=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
one_deck=4*cards
decks=4
game_deck=copy.deepcopy(decks*one_deck)
print(game_deck)
WIDTH=600
HEIGHT=900
screen=pygame.display.set_mode([WIDTH,HEIGHT])#window for the game
pygame.display.set_caption('Pygame Blackjack')#caption or name of the window
fps=60
timer=pygame.time.Clock()#uses the fps
font=pygame.font.font('freesansbold.ttf',44)
 
#Main game loop
run =True
while run:
    #run game at fps and fill screen with bg color
    timer.tick(fps)
    screen.fill('white')
    #if quit pressed, then exit game
   

