import pygame
import os
import var as v
import sprites as s

pygame.init()

pygame.display.set_caption('Squares Fight')

allSprites = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()

player1 = s.Player(v.blueImage)
player2 = s.Player(v.orangeImage)

player1.rect.x = v.blueX
player1.rect.y = v.blueY
player2.rect.x = v.orangeX
player2.rect.y = v.orangeY

allSprites.add(player1, player2)

while v.loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v.loop = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player1.right(3)

    if keys[pygame.K_UP]:
        player1.up(3)

    if keys[pygame.K_DOWN]:
        player1.down(3)

    if keys[pygame.K_LEFT]:
        player1.left(3)

    if keys[pygame.K_d]:
        player2.right(3)

    if keys[pygame.K_s]:
        player2.down(3)

    if keys[pygame.K_w]:
        player2.up(3)

    if keys[pygame.K_a]:
        player2.left(3)

    if keys[pygame.K_e]:
        player2.dashright(20)

    if keys[pygame.K_q]:
        player2.dashleft(20)

    if keys[pygame.K_SLASH]:
        player1.dashleft(20)

    if keys[pygame.K_RSHIFT]:
        player1.dashright(20)

    if keys[pygame.K_SPACE]:
        bulletGroup.add(s.Bullet(v.blueImage, 250, 250))

    collision = pygame.sprite.collide_rect(player1, player2)
    
    if collision == True:
        allSprites.remove(player1, player2)
        v.text = v.font.render('o noes', True, v.white)
        pygame.display.set_caption('They destroyed eachother, space to retry')
        v.again = True
    if v.again == True and keys[pygame.K_SPACE]:
        allSprites.remove(player1, player2)
        v.text = v.font.render('Fight!', True, v.white)
        pygame.display.set_caption('Squares Fight!')
        v.again = False
        player1.rect.x = v.blueX
        player1.rect.y = v.blueY
        player2.rect.x = v.orangeX
        player2.rect.y = v.orangeY
        allSprites.add(player1, player2)
        

    allSprites.update()
    bulletGroup.update(3)

    v.screen.fill(v.black)
    v.screen.blit(v.text,
               (250 - v.text.get_width() // 2, 240 - v.text.get_height() // 2))
    allSprites.draw(v.screen)

    pygame.display.flip()
    v.clock.tick(v.FPS)
pygame.quit()
