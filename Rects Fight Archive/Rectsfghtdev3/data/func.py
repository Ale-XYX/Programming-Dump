import pygame
import datetime
import media as m
import var as v

pygame.init()

def get(type1, insert):
    if type1 == 'char':
        image = m.GAME_MEDIA[insert]['player_image']
        color = m.GAME_MEDIA[insert]['color']
        text = v.font.render(insert, True, color)
        return image, text
    elif type1 == 'time':
        if insert <= 10:
            return v.font4.render(str(round(insert, 1)), True, v.red)
        else:
            return v.font.render(str(round(insert, 1)), True, v.white)
    
print(str(datetime.datetime.now().strftime("%H:%M:%S")) + '@' + 'FUNC: ' + 'Loaded Get()')
        
