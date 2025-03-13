import sys
import random
from functools import partial

map=[]
def pos_trans(x,y):
    index=y*width+x
    return index
        
global width,height

width=10
height=30
for i in range(0,width*height):
    map.append({'map_pos':[i%width,i//width],'is_obs':False,'color':'white'})
for i in map[pos_trans(9,2)]['map_pos']:
    print(type(i))
print(type(map[pos_trans(9,2)]['map_pos']),map[pos_trans(9,2)]['color'])
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
        return [[x,y],[x,y-1],[x+1,y],[x+1,y-1]],'yellow'
    if direction=='left':
        return [[x,y],[x+1,y],[x+1,y-1],[x+2,y-1]],'yellow'
    if  direction=='right':
        return [[x,y],[x,y-1],[x+1,y],[x+1,y-1]],'yellow'

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
init_pos=[4,0]
graph_size=28
map_size=30
width=10
height=20
init_direction='up'
l=[partial(shape_1,init_pos[0],init_pos[1],init_direction),partial(shape_2,init_pos[0],init_pos[1],init_direction),partial(shape_3,init_pos[0],init_pos[1],init_direction)]
shape_list,color=random.choice(l)()
print(shape_list,color)