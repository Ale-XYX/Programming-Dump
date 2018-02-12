import media as m
import var as v
import random

def GET_RANDOM():
    i = random.randrange(0, 6)
    DICT = {
        0: v.blue,
        1: v.orange,
        2: v.green,
        3: v.purple,
        4: v.red
        5: v.yellow
        6: v.white
    return DICT[i]      
        
GAME_DICT = {
    'BLUE': {
        'COLOR': v.blue,
        'PLAYER_IMAGE': m.MEDIA['
