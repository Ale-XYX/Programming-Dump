if __name__ == '__main__':
    import pygame
    import sys
    import datetime
    logat = str(datetime.datetime.now().time()) + '@' + 'APP: '
    print(logat + ': ' + 'Loading Rects Fight V1.5')
    sys.path.insert(0, './data')
    import game as g
    print('Starting')
    pygame.init()
    g.title()
    g.char_select()
    g.main()
    pygame.quit()
