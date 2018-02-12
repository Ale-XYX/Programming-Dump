# CLIENT 
if __name__ == '__main__':
    import sys
    import pygame

    sys.path.insert(0, './data')
    import game

    pygame.init()
    game.main()
    pygame.quit()
