import pygame
import random
import sys
import copy
import pygame as pg
from functools import partial
from pygame.locals import *

def draw_graph(graph_list,graph_size,map_size,color,screen):
    for z in graph_list:
        pygame.draw.rect(screen,color, [z[0]*map_size, z[1]*map_size,graph_size ,graph_size], 0)

def draw_text(text, font, color, screen, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_obj, text_rect)

def test_shape(x,y,direction):
    if direction=='up':
        return [[_x, y] for _x in range(0, 10)],'red'

def shape_1(x,y,direction):
    if direction == 'up':
        return [[x,y],[x+1,y],[x+2,y],[x+3,y]],'red'
    if direction == 'down':
        return [[x,y],[x,y-1],[x,y-2],[x,y-3]],'red'
    if direction=='left':
        return [[x,y],[x+1,y],[x+2,y],[x+3,y]],'red'
    if  direction=='right':
        return [[x,y],[x+1,y],[x+2,y],[x+3,y]],'red'

def shape_2(x,y,direction):
    if direction == 'up':
        return [[x,y],[x+1,y],[x,y-1],[x+1,y-1]],'blue'
    if direction == 'down':
        return [[x,y],[x+1,y],[x,y-1],[x+1,y-1]],'blue'
    if direction=='left':
        return [[x,y],[x+1,y],[x,y-1],[x+1,y-1]],'blue'
    if  direction=='right':
        return [[x,y],[x+1,y],[x,y-1],[x+1,y-1]],'blue'

def shape_3(x,y,direction):
    if direction == 'up':
        return [[x,y],[x,y-1],[x+1,y],[x+2,y]],'green'
    if direction == 'down':
        return [[x,y],[x,y-1],[x,y-2],[x+1,y-2]],'green'
    if direction=='left':
        return [[x,y],[x+1,y],[x+2,y],[x+2,y+1]],'green'
    if  direction=='right':
        return [[x,y],[x+1,y],[x+1,y-1],[x+1,y-2]],'green'

def shape_4(x,y,direction):
    if direction == 'up':
        return [[x,y],[x+1,y],[x+1,y+1],[x+2,y+1]],'black'
    if direction == 'down':
        return [[x,y],[x,y-1],[x+1,y-1],[x+1,y-2]],'black'
    if direction=='left':
        return [[x,y],[x+1,y],[x+1,y+1],[x+2,y+1]],'black'
    if  direction=='right':
        return [[x,y],[x,y-1],[x+1,y-1],[x+1,y-2]],'black'

def shape_5(x,y,direction):
    if direction == 'up':
        return [[x,y],[x+1,y],[x+1,y-1],[x+2,y-1]],'yellow'
    if direction == 'down':
        return [[x,y],[x,y-1],[x+1,y-1],[x+1,y-2]],'yellow'
    if direction=='left':
        return [[x,y],[x+1,y],[x+1,y-1],[x+2,y-1]],'yellow'
    if  direction=='right':
        return [[x,y],[x,y-1],[x+1,y-1],[x+1,y-2]],'yellow'

def shape_6(x,y,direction):
    if direction == 'up':
        return [[x,y],[x+1,y],[x+1,y-1],[x+2,y]],'gold'
    if direction == 'down':
        return [[x,y],[x,y-1],[x,y-2],[x+1,y-1]],'gold'
    if direction=='left':
        return [[x,y],[x+1,y],[x+1,y-1],[x+2,y]],'gold'
    if  direction=='right':
        return [[x,y],[x+1,y-1],[x+1,y],[x+1,y+1]],'gold'

def shape_7(x,y,direction):
    if direction == 'up':
        return [[x,y],[x+1,y],[x+2,y],[x+2,y-1]],'violet'
    if direction == 'down':
        return [[x,y],[x,y-1],[x,y-2],[x+1,y]],'violet'
    if direction=='left':
        return [[x,y],[x,y-1],[x+1,y-1],[x+2,y-1]],'violet'
    if  direction=='right':
        return [[x,y],[x+1,y],[x+1,y+1],[x+1,y+2]],'violet'


def create_map():
    map=[]
    for i in range(0,width*height):
        map.append({'map_pos':[i%width,i//width],'is_obs':False,'color':'white'})
    return map

def draw_map(map_data,graph_size,map_size,screen):
    for i in range(0,width):
        for j in range(0,height):
            if map_data[pos_trans(i,j,width)]['is_obs']:
                pygame.draw.rect(screen,map_data[pos_trans(i,j,width)]['color'], [map_data[pos_trans(i,j,width)]['map_pos'][0]*map_size, map_data[pos_trans(i,j,width)]['map_pos'][1]*map_size,graph_size ,graph_size], 0)

def pos_trans(x,y,width):
    index=y*width+x
    return index

def graph_fall(fall_speed,shape_list,is_fall):
    if is_fall:
        for i in shape_list:
            i[1]=i[1]+fall_speed
            i[1]= min(i[1], 19)
        return shape_list
    else:
        return shape_list
        

def isfall(map_data,shape_list,width,is_fall,color,cur_speed,fall_speed):
    for i in shape_list:
        if i[1]<height-1:
            if cur_speed==fall_speed*2:
                if map_data[pos_trans(i[0],i[1]+cur_speed+1,width)]['is_obs']:
                    is_fall=False
                    for j in shape_list:
                        map_data[pos_trans(j[0],j[1]+cur_speed-1+1,width)]['is_obs']=True
                        map_data[pos_trans(j[0],j[1]+cur_speed-1+1,width)]['color']=color
            else:
                if map_data[pos_trans(i[0],i[1]+cur_speed,width)]['is_obs']:
                    is_fall=False
                    for j in shape_list:
                        map_data[pos_trans(j[0],j[1]+cur_speed-1,width)]['is_obs']=True
                        map_data[pos_trans(j[0],j[1]+cur_speed-1,width)]['color']=color                
        elif  i[1] ==height-1:
            is_fall=False
            for j in shape_list:
                map_data[pos_trans(j[0],j[1],width)]['is_obs']=True
                map_data[pos_trans(j[0],j[1],width)]['color']=color
        
    return is_fall,map_data

def when_remove(map_data,width):
    for i in range(19,-1,-1):
        count=0
        for j in range(0,10):
            if map_data[pos_trans(j,i,width)]['is_obs']:
                count+=1
        if count==width:
            return True,i
    return False,None
        
def line_remove(map_data,width,score,is_remove,sound_1):
    is_remove,line_num=when_remove(map_data,width)
    if is_remove:
        sound_1.play()
        score+=1
        for i in range(line_num,-1,-1):
            if i >0:
                for j in range(0,10):
                    map_data[pos_trans(j,i,width)]['is_obs'],map_data[pos_trans(j,i,width)]['color']=map_data[pos_trans(j,i-1,width)]['is_obs'],map_data[pos_trans(j,i-1,width)]['color']
            else:
                for j in range(0,10):
                    map_data[pos_trans(j,i,width)]['is_obs'],map_data[pos_trans(j,i,width)]['color']=False,'white'
        is_remove=False
        return map_data,score,is_remove
    else:
        is_remove=False
        return map_data,score,is_remove

def left_move(shape_list,map_data,width):
    if shape_list[0][0]>0:
        count=0
        for i in shape_list:
            if map_data[pos_trans(i[0]-1,i[1],width)]['is_obs']:
               count+=1
        if count==0:
            can_move=True 
        else:
            can_move=False
    else:
        can_move=False
    if can_move:
        for i in shape_list:
            i[0]=i[0]-1
        return shape_list
    else:
        return shape_list

def right_move(shape_list,map_data,width):
    if shape_list[-1][0]<width-1:
        count=0
        for i in shape_list:
            if map_data[pos_trans(i[0]+1,i[1],width)]['is_obs']:
               count+=1
        if count==0:
            can_move=True 
        else:
            can_move=False
    else:
        can_move=False
    if can_move:
        for i in shape_list:
            i[0]=i[0]+1
        return shape_list
    else:
        return shape_list

def CheckSetCd(cd_list, idx, cd):
    cur_tick = pygame.time.get_ticks()
    if cur_tick - cd_list[idx] > cd:
        cd_list[idx] = cur_tick
        return True
    return False

def game_win():
    screen.fill('black')
    draw_text("You win", font,'green', screen, (map_size*width+90)//2, (map_size*height)//2)
    pygame.display.update()

def game_over():
    screen.fill('black')
    draw_text("You are dead", font,'red', screen, (map_size*width+90)//2, (map_size*height)//2)
    pygame.display.update()

def win_or_over(map_data,score,Target_score):
    for i in range(0,10):
        if map_data[i]['is_obs']:
            running = False
            game_over()
            pygame.time.wait(2000)
            pygame.quit()
    if score==Target_score:
        running = False
        game_win()
        pygame.time.wait(2000)
        pygame.quit()

pygame.init()
sound=pygame.mixer.Sound("C:\\Users\\hp\\Desktop\\my_program\\Tetris\\play_music.mp3")
sound_1=pygame.mixer.Sound("C:\\Users\\hp\\Desktop\\my_program\\Tetris\\line_move.mp3")
fall_speed=1
plus_speed=2
running=True
is_fall=False
Target_score=10
map_data=[]
init_pos=[4,0]
graph_size=28
map_size=30
score=0
width=10
height=20
is_remove=False
font = pygame.font.SysFont(None, 30)
init_direction='up'
map_data=create_map()
screen=pygame.display.set_mode((map_size*width+90,map_size*height))
pygame.display.set_caption("俄罗斯方块测试版")

global_cd_list = [ 0 for _idx in range(3)]
l=[partial(shape_1,init_pos[0],init_pos[1],init_direction),partial(shape_2,init_pos[0],init_pos[1],init_direction),partial(shape_3,init_pos[0],init_pos[1],init_direction),partial(shape_4,init_pos[0],init_pos[1],init_direction),partial(shape_5,init_pos[0],init_pos[1],init_direction),partial(shape_6,init_pos[0],init_pos[1],init_direction),partial(shape_7,init_pos[0],init_pos[1],init_direction)]
cnt = 0
while running:
    # 清除屏幕
    screen.fill('white')
   # pygame.mixer.music.load("C:\\Users\\hp\\Desktop\\my_program\\Tetris\\play_music.mp3")
    sound.play(-1)
    draw_text(str(score), font, 'red', screen,width*map_size+30 ,height*map_size//2 )
    pygame.draw.line(screen, 'black',(map_size*width,0),(map_size*width,map_size*height), 3)
    map_data,score,is_remove=line_remove(map_data,width,score,is_remove,sound_1)
    win_or_over(map_data,score,Target_score)
    pygame.key.set_repeat(10, 15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not is_fall:
        graph_list,color=random.choice(l)()
        is_fall=True
    keys = pygame.key.get_pressed()
    if CheckSetCd(global_cd_list, 2, 100): 
        if keys[pygame.K_w]:
            direction_list=['up','down','right','left']
            init_direction=direction_list[cnt]
            cnt+=1
            cnt = cnt % len(direction_list)
            #init_direction=random.choice(direction_list)
            if color=='red':
                graph_list,color=shape_1(graph_list[0][0],graph_list[0][1],init_direction)
            if color=='blue':
                graph_list,color=shape_2(graph_list[0][0],graph_list[0][1],init_direction)
            if color=='green':
                graph_list,color=shape_3(graph_list[0][0],graph_list[0][1],init_direction)
            if color=='black':
                graph_list,color=shape_4(graph_list[0][0],graph_list[0][1],init_direction)
            if color=='yellow':
                graph_list,color=shape_5(graph_list[0][0],graph_list[0][1],init_direction)
            if color=='gold':
                graph_list,color=shape_6(graph_list[0][0],graph_list[0][1],init_direction)
            if color=='violet':
                graph_list,color=shape_7(graph_list[0][0],graph_list[0][1],init_direction)
    if keys[pygame.K_s]:
        if graph_list[0][1]<17:
            cur_speed = fall_speed * 2
            is_fall,map_data=isfall(map_data,graph_list,width,is_fall,color,cur_speed,fall_speed)
        else:
            cur_speed =fall_speed
            is_fall,map_data=isfall(map_data,graph_list,width,is_fall,color,cur_speed,fall_speed)
    else:
        cur_speed =fall_speed
        is_fall,map_data=isfall(map_data,graph_list,width,is_fall,color,cur_speed,fall_speed)
    if CheckSetCd(global_cd_list, 0, 100): 
        if keys[pygame.K_a] :
            graph_list=left_move(graph_list,map_data,width)
        elif keys[pygame.K_d] :
            graph_list=right_move(graph_list,map_data,width)

    is_fall,map_data=isfall(map_data,graph_list,width,is_fall,color,cur_speed,fall_speed)
    draw_graph(graph_list,graph_size,map_size,color,screen)
    draw_map(map_data,graph_size,map_size,screen)
    
    if CheckSetCd(global_cd_list, 1, 350): 
        graph_list=graph_fall(cur_speed,graph_list,is_fall)
    pygame.mixer.music.get_busy()
    pygame.display.flip()

pygame.mixer.music.stop()  
pygame.quit()


#######
#######