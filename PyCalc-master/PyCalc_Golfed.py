from pygame import*;init()
class Globals:screen=display.set_mode((260,400));calculator_sheet=image.load('./media/operator_sheet.png');icon=image.load('./media/icon.png');superloop=True;result=None
display.set_caption('PyCalc');display.set_icon(Globals.icon);loop=True;clock=time.Clock();font,font_small=font.SysFont(None,40),font.SysFont(None,20);RECT_DICT = {'zero':Rect(74,286,50,50),'one':Rect(12,225,50,50),'two':Rect(74,225,50,50),'three':Rect(136,225,50,50),'four':Rect(12,164,50,50),'five':Rect(74,164,50,50),'six':Rect(136,164,50,50),'seven':Rect(12,103,50,50),'eight':Rect(74,103,50,50),'nine':Rect(136,103,50,50),'add':Rect(198,103,50,50),'sub':Rect(198,164,50,50),'mul':Rect(198,225,50,50),'div':Rect(198,286,50,50),'equal':Rect(198,347,50,50),'reset':Rect(12, 286, 25, 50),'clear':Rect(37, 286, 25, 50),'negative':Rect(136, 286, 50, 50)}
while Globals.superloop:
    BLACK=(0,0,0);WHITE=(255,255,255);ORANGE=(255,191,0);RED=(211,0,0);eq_storage,op_storage=[],[];num_st,op_st,op_str='','','';toggle=False;num_txt=None;num_rects=[RECT_DICT['zero'],RECT_DICT['one'],RECT_DICT['two'],RECT_DICT['three'], RECT_DICT['four'], RECT_DICT['five'],RECT_DICT['six'],RECT_DICT['seven'],RECT_DICT['eight'],RECT_DICT['nine'],RECT_DICT['negative']];op_rects=list(zip([RECT_DICT['add'],RECT_DICT['sub'],RECT_DICT['div'],RECT_DICT['mul']],'+-/*'));sp_rects=[RECT_DICT['clear'],RECT_DICT['reset']]
    while loop:
        for e in event.get():
            if e.type==QUIT:loop=False;Globals.superloop =False
            elif e.type==MOUSEBUTTONDOWN:
                for i, rect in enumerate(num_rects):
                    if num_rects[i].collidepoint(e.pos):
                        if i==0 and num_st=='':num_st+='-'
                        elif i==10:pass
                        else:num_st+=str(i)
                for rect, operator in op_rects:
                    if rect.collidepoint(e.pos):op_storage.append(operator);eq_storage.append(num_st);num_st=''
                for i, rect in enumerate(sp_rects):
                    if sp_rects[i].collidepoint(e.pos):
                        if i==0:num_st='';break
                        elif i==1:loop=False;break
                if RECT_DICT['equal'].collidepoint(e.pos):
                    try:eq_storage.append(num_st);num_st='';eq_generate=''.join(f"{a}{b}" for a,b in zip(eq_storage,op_storage))+str(eq_storage[-1]);Globals.result=eval(eq_generate);toggle=True
                    except SyntaxError:Globals.result='Invalid';toggle=True
                    except ZeroDivisionError:Globals.result='Infinity';toggle=True
        if not toggle:num_txt=font.render(num_st,True,WHITE)
        elif toggle:num_txt=font.render(str(Globals.result),True,ORANGE)
        op_txt=font_small.render(str(op_storage),True,WHITE);Globals.screen.fill(BLACK);Globals.screen.blit(Globals.calculator_sheet,(0,100));Globals.screen.blit(num_txt,(12,50));Globals.screen.blit(op_txt,(12,10));display.flip();clock.tick(60)
