# Import
import pygame

pygame.init()

class Globals:
    screen = pygame.display.set_mode((260, 400))
    calculator_sheet = pygame.image.load('./media/operator_sheet.png')
    icon = pygame.image.load('./media/icon.png')
    superloop = True
    result = None


pygame.display.set_caption('PyCalc')
pygame.display.set_icon(Globals.icon)


def main():
    # Game variables
    loop = True
    clock = pygame.time.Clock()
    font, font_small = pygame.font.SysFont(None, 40), pygame.font.SysFont(None, 20)
    # Rectangles
    RECT_DICT = {
        'zero': pygame.Rect(74, 286, 50, 50), 'one': pygame.Rect(12, 225, 50, 50),
        'two': pygame.Rect(74, 225, 50, 50), 'three': pygame.Rect(136, 225, 50, 50),
        'four': pygame.Rect(12, 164, 50, 50), 'five': pygame.Rect(74, 164, 50, 50),
        'six': pygame.Rect(136, 164, 50, 50), 'seven': pygame.Rect(12, 103, 50, 50),
        'eight': pygame.Rect(74, 103, 50, 50), 'nine': pygame.Rect(136, 103, 50, 50),
        'add': pygame.Rect(198, 103, 50, 50), 'sub': pygame.Rect(198, 164, 50, 50),
        'mul': pygame.Rect(198, 225, 50, 50), 'div': pygame.Rect(198, 286, 50, 50),
        'equal': pygame.Rect(198, 347, 50, 50), 'reset':  pygame.Rect(12, 286, 25, 50),
        'clear': pygame.Rect(37, 286, 25, 50), 'negative': pygame.Rect(136, 286, 50, 50)
    }
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    ORANGE = (255, 191, 0)
    RED = (211, 0, 0)
    # Data storage
    eq_storage, op_storage = [], []
    num_st, op_st, op_str = '', '', ''
    toggle = False
    num_txt = None
    # Handling input
    num_rects = [RECT_DICT['zero'], RECT_DICT['one'], RECT_DICT['two'],
                RECT_DICT['three'], RECT_DICT['four'], RECT_DICT['five'],
                RECT_DICT['six'], RECT_DICT['seven'], RECT_DICT['eight'],
                RECT_DICT['nine'], RECT_DICT['negative']]
    op_rects = list(zip([RECT_DICT['add'], RECT_DICT['sub'], RECT_DICT['div'], RECT_DICT['mul']], '+-/*'))
    sp_rects = [RECT_DICT['clear'], RECT_DICT['reset']]

    # Game loop
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                Globals.superloop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handling number input
                for i, rect in enumerate(num_rects):
                    if num_rects[i].collidepoint(event.pos):
                        # After:
                        # Same as before
                        if i == 10 and num_st == '':
                            num_st += '-'
                        # Now if i == 10, it passes [ends] the function
                        elif i == 10:
                            pass
                        # same as before
                        else:
                            num_st += str(i)
                # Handling operator input
                for rect, operator in op_rects:
                    if rect.collidepoint(event.pos):
                        op_storage.append(operator)
                        eq_storage.append(num_st)
                        num_st = ''
                # Handling special input
                for i, rect in enumerate(sp_rects):
                    if sp_rects[i].collidepoint(event.pos):
                        if i == 0:
                            num_st = ''
                            break
                        elif i == 1:
                            loop = False
                            break
                # Handling equal input
                if RECT_DICT['equal'].collidepoint(event.pos):
                    try:
                        eq_storage.append(num_st)
                        num_st = ''
                        eq_generate = "".join(f"{a}{b}" for a, b in zip(eq_storage, op_storage)) + str(eq_storage[-1])
                        Globals.result = eval(eq_generate)
                        print(str(Globals.result))
                        toggle = True
                    except SyntaxError:
                        Globals.result = 'Invalid'
                        toggle = True
                    except ZeroDivisionError:
                        Globals.result = 'Infinity'
                        toggle = True

        # Text rendering
        if not toggle:
            num_txt = font.render(num_st, True, WHITE)
        elif toggle:
            num_txt = font.render(str(Globals.result), True, ORANGE)
        op_txt = font_small.render(str(op_storage), True, WHITE)

        Globals.screen.fill(BLACK)
        Globals.screen.blit(Globals.calculator_sheet, (0, 100))
        Globals.screen.blit(num_txt, (12, 50))
        Globals.screen.blit(op_txt, (12, 10))

        pygame.display.flip()
        clock.tick(60)


# Game Sequence
if __name__ == '__main__':
    while Globals.superloop:
        main()
    pygame.quit()
