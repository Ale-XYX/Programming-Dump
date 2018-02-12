import pygame
import variables as v
import sprites as s
import functions as f

pygame.init()
pygame.display.set_caption('Squares Fight')

v.allSprites.add(v.player1, v.player2)

# ----- Main Game ------

while v.loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v.loop = False
            
    # Keymap logic
    
    if v.keys[pygame.K_RIGHT]:
        v.player1.right(3)

    if v.keys[pygame.K_UP]:
        v.player1.up(3)

    if v.keys[pygame.K_DOWN]:
        v.player1.down(3)

    if v.keys[pygame.K_LEFT]:
        v.player1.left(3)

    if v.keys[pygame.K_d]:
        v.player2.right(3)

    if v.keys[pygame.K_s]:
        v.player2.down(3)

    if v.keys[pygame.K_a]:
        v.player2.left(3)

    if v.keys[pygame.K_w]:
        v.player2.up(3)

    if v.keys[pygame.K_e]:
        v.player2.dashright(20)

    if v.keys[pygame.K_q]:
        v.player2.dashleft(20)

    if v.keys[pygame.K_SLASH]:
        v.player1.dashleft(20)

    if v.keys[pygame.K_RSHIFT]:
        player1.dashright(20)

    # Collision/Quitting logic


    #Drawing
        
    v.allSprites.update()
    v.screen.fill(v.black)
    v.allSprites.draw(v.screen)

    pygame.display.flip()
    v.clock.tick(v.FPS)
    
pygame.quit()
