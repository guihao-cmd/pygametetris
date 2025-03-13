import pygame
import random
import sys
import copy

def draw_rect(screen,x,y):
    pygame.draw.rect(screen, 'black', [x*size, y*size, size, size], 0)

def shape_1(x,y):
    return [[x,y],[x-1,y],[x-2,y],[x-2,y+1]]

def shape_2(x,y):
    return [[x,y],[x+1,y],[x,y-1],[x-1,y-1]]

def shape_3(x,y):
    return  [[x,y],[x-1,y],[x+1,y],[x,y-1]]


def shape_4(x,y):
    return [[x,y],[x+1,y],[x+2,y],[x+3,y]]       

def shape_5(x,y):
    return [[x,y],[x+1,y],[x,y-1],[x+1,y-1]]

def create_map(map_data,map_data_line):
    for j in range(0,10):
        map_data_line.append(0)
    for i in range(0,20):
        map_data.append(copy.deepcopy(map_data_line))
    return map_data and map_data_line
  

def all_down(map_data,map_data_line,start_line_num):
    for i in range(start_line_num,-1,-1):
        if i ==0:
            map_data[0]=copy.deepcopy(map_data_line)
        else:
            map_data[i]=copy.deepcopy(map_data[i-1])
    return map_data

def is_clean(map_data,map_data_line):
    for i in range(19,-1,-1):
        count=0
        for j in range(0,10):
            if map_data[i][j]==1:
                count+=1
        if  count==10:
            start_line_num=i
            all_down(map_data,map_data_line,start_line_num)
    

def draw_map(screen,map_data):
    for i in range(19,-1,-1):
        for j in range(0,10):
            if map_data[i][j]==1:
                draw_rect(screen,j,i)
        
def fall(shape_list,fall_speed):
    for i in shape_list:
        if have_down:
            i[1]=i[1]+fall_speed
        else:
            return 
    return shape_list

def draw_graph(shape_list,screen):
    for i in shape_list:
        draw_rect(screen,i[0],i[1])

def shape_left(shape_list):
    for i in shape_list:
        if i[0]==0:
            return shape_list
        elif map_data[i[1]][i[0]-1]==1 or i[0]==0:
            return shape_list
        else:
            i[0]=i[0]-1
    return shape_list

def shape_right(shape_list):
    for i in shape_list:
        if i[0]==9:
            return shape_list
        elif map_data[i[1]][i[0]+1]==1 or i[0]==9:
            return shape_list
        else:
            i[0]+=1
    return shape_list

def is_down(shape_list,map_data,have_down):
    touch_bottom = False
    for i in shape_list:
        if i[1]==19:
            touch_bottom=True
        if keys[pygame.K_s]:
            if  map_data[i[1]+2][i[0]]==1 or i[1]==19:
                touch_bottom=True
        elif map_data[i[1]+1][i[0]]==1 or i[1]==19:
                touch_bottom=True
    if touch_bottom:
        for j in shape_list:
            map_data[j[1]][j[0]]=1
    return map_data, not touch_bottom ,shape_list

pygame.init()
size=30
width=10
height=20
start_line_num=0
map_data=[]
map_data_line=[]
shape_list=[]
running=True
fall_speed=1
graph1=shape_1(5,0)
graph2=shape_2(5,0)
graph3=shape_3(5,0)          
graph4=shape_4(5,0)
graph5=shape_5(5,0)
print(len(shape_list))


graph_list=[graph1,graph2,graph3,graph4,graph5]
create_map(map_data,map_data_line)
have_down= False
screen=pygame.display.set_mode((size*width,size*height))
last_tick = pygame.time.get_ticks()
while running:
    screen.fill('white')
    draw_map(screen,map_data)
    draw_graph(shape_list,screen)
    #is_clean(map_data,map_data_line)
    pygame.key.set_repeat(10, 15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        fall_speed=fall_speed*2
        fall(shape_list,fall_speed)
    else:
        fall_speed=fall_speed

    if keys[pygame.K_a] :
        shape_left(shape_list)
    elif keys[pygame.K_d] :
        shape_right(shape_list)
    cur_tick = pygame.time.get_ticks()
    if (cur_tick - last_tick) < 200:
        continue
    last_tick = cur_tick        

    if not have_down:
        temp_list = random.choice(graph_list)
        shape_list = copy.deepcopy(temp_list)
        have_down=True    
    #fall(shape_list,fall_speed)
    map_data,have_down,shape_list=is_down(shape_list,map_data,have_down)
 

    pygame.display.flip()  
