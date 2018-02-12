import pygame
import variables as v
import sprites as s
pygame.init()

def onCollision():
    pygame.display.set_caption('They Destroyed Eachother! SPACE: Restart')
    v.allSprites.remove(v.player1, v.player2)
    v.again = True
    
def collisionConfirm():
    pygame.display.set_caption('Squares Fight!')
    v.allSprites.add(v.player1, v.player2)
    v.again = False

def quit():
    pygame.display.set_caption('Quitting? TAB: Cancel, ESC: Quit')
    v.checkIfLeave = True

def quitCancel():
    pygame.display.set_caption('Squares Fight!')
    v.checkIfLeave = True
    
