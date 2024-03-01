from js import document, window, Image, console
import js
import world
from pyodide import create_proxy
import datetime as dt
import asyncio
import user_interact

lastTime = 4
fps = 30
fpsInterval = 1000 / fps

canvas = document.getElementById('Canvas')
canvas.width = 500
canvas.height = 500
ctx = canvas.getContext('2d')
console.log("Hey there, from 'console.log' inside PyScript!")
class DrawImage: # main에서만 js꺼 다룰 수 있음!
    def __init__(self,obj) -> None:
        self.image = Image.new()
        self.image.src = ""
        self.x = obj.x
        self.y = obj.y
        self.height = obj.height
        self.width = obj.width
        self.img_set_len = {}
        #self.img_set_len
        self.pic_num_set = {}
        self.state = "default"
        print(obj)
        for k,v in obj.img_set.items():
            self.img_set_len[k] = len(obj.img_set[k])
            self.pic_num_set[k] = 0
    
    
    def draw(self, obj):
        self.x = obj.x
        self.y = obj.y
        self.width = obj.width
        self.height = obj.height
        self.state = obj.state
        img_len = self.img_set_len[self.state]
        
        
        self.pic_num_set[self.state] = self.pic_num_set[self.state] + 1 if self.pic_num_set[self.state] < img_len-1 else 0 
        
        self.image.src = obj.img_set[self.state][self.pic_num_set[self.state]]
        #print(self.pic_num)
        ctx.drawImage(self.image, self.x, self.y, self.width, self.height)

# 방향애따라 그리는 것도 달라야함
# 이미지set있다면 그거 따라가기
def update_draw(obj_world,obj_js):
    obj_js.draw(obj_world)
    obj_world.update_position()
def check_out(obj):
    if obj.x < -10:
        return True
    if obj.x + obj.width > canvas.width+10:
        return True
    if obj.y < -10:
        return True
    if obj.y + obj.height > canvas.height+10 :
        return True
    return False

# 게임 완료 상태를 서버에 알리기
def notify_server_game_completed():
    window.sendCompletionMessage()

def UserInitCode():
    state = 0
#$user_init_start
    # Enter your code here
    ㅁㄴㅇ
#$user_init_out
def UserLoopCode():
    state=0
#$user_loop_start
    
#$user_loop_out


################################
rabbit_img_set ={
   "default": ['./assets/rabbit/front/1.png','./assets/rabbit/front/2.png','./assets/rabbit/front/3.png','./assets/rabbit/front/4.png'],
   "front": ['./assets/rabbit/front/1.png','./assets/rabbit/front/2.png','./assets/rabbit/front/3.png','./assets/rabbit/front/4.png'],
    "back":['./assets/rabbit/back/1.png','./assets/rabbit/back/2.png','./assets/rabbit/back/3.png','./assets/rabbit/back/4.png'],
    "left":['./assets/rabbit/left/1.png','./assets/rabbit/left/2.png','./assets/rabbit/left/3.png','./assets/rabbit/left/4.png'],
    "right":['./assets/rabbit/right/1.png','./assets/rabbit/right/2.png','./assets/rabbit/right/3.png','./assets/rabbit/right/4.png'],
}
knight_img_set ={
    "default":['./assets/knight/right/Warrior_Blue_1.png','./assets/knight/right/Warrior_Blue_2.png','./assets/knight/right/Warrior_Blue_3.png',
               './assets/knight/right/Warrior_Blue_4.png','./assets/knight/right/Warrior_Blue_5.png','./assets/knight/right/Warrior_Blue_6.png',],
    "right":['./assets/knight/right/Warrior_Blue_1.png','./assets/knight/right/Warrior_Blue_2.png','./assets/knight/right/Warrior_Blue_3.png',
               './assets/knight/right/Warrior_Blue_4.png','./assets/knight/right/Warrior_Blue_5.png','./assets/knight/right/Warrior_Blue_6.png',],
    "left":['./assets/knight/left/Warrior_Blue_1.png','./assets/knight/left/Warrior_Blue_2.png','./assets/knight/left/Warrior_Blue_3.png',
               './assets/knight/left/Warrior_Blue_4.png','./assets/knight/left/Warrior_Blue_5.png','./assets/knight/left/Warrior_Blue_6.png',]
}
Castle_img_set = {
    "default":['./assets/Buildings/Castle/Castle_Blue.png']
}
House_img_set = {
    "default" : ['./assets/Buildings/House/House_Blue.png']
}
Tower_img_set ={
    "default" : ['./assets/Buildings/Tower/Tower_Blue.png']
}
background_img_set={
    "default" : ['./assets/background/grid_tile.png']
}
Gem_img_set = {
    "default" : ['./assets/item/gem/gem-1.png','./assets/item/gem/gem-2.png','./assets/item/gem/gem-3.png','./assets/item/gem/gem-4.png','./assets/item/gem/gem-5.png']
}
Gold_img_set = {
    "default": ['./assets/item/gold/G_Spawn.png','./assets/item/gold/G_Spawn (1).png','./assets/item/gold/G_Spawn (2).png','./assets/item/gold/G_Spawn (3).png'
                ,'./assets/item/gold/G_Spawn (4).png','./assets/item/gold/G_Spawn (5).png','./assets/item/gold/G_Spawn (6).png']
}
Tree_img_set = {
    "default" : ['./assets/objects/tree/Tree.png','./assets/objects/tree/Tree (1).png','./assets/objects/tree/Tree (2).png','./assets/objects/tree/Tree (3).png']
}
Sheep_img_set={
    "right":['./assets/objects/sheep/right/HappySheep_Bouncing (1).png','./assets/objects/sheep/right/HappySheep_Bouncing (2).png',
             './assets/objects/sheep/right/HappySheep_Bouncing (3).png','./assets/objects/sheep/right/HappySheep_Bouncing (4).png',
             './assets/objects/sheep/right/HappySheep_Bouncing (5).png','./assets/objects/sheep/right/HappySheep_Bouncing.png'],
    "left":['./assets/objects/sheep/left/HappySheep_Bouncing (1).png','./assets/objects/sheep/left/HappySheep_Bouncing (2).png',
             './assets/objects/sheep/left/HappySheep_Bouncing (3).png','./assets/objects/sheep/left/HappySheep_Bouncing (4).png',
             './assets/objects/sheep/left/HappySheep_Bouncing (5).png','./assets/objects/sheep/left/HappySheep_Bouncing.png'],
}
castle_set = []
World_Walls = []
#__init__(self, x, y, w, h,hit_x,hit_y,hit_w,hit_h,direction, dx, dy,state,img_set):

# hit box!
# 움직ㅇ리때 hit box도 움직여야함 
# 실제 자기 box 다름!
# hit x,y: hit box의 시작좌표
# hit_w _h : hit box의 width와 height

warrior = world.Hero(0,0,50,50,10,10,30,30,"S",0,0,"default",knight_img_set)

gem = world.Item(413,413,25,25,413,413,25,25,"S",0,0,"default",Gem_img_set)
gold = world.Item(413,113,25,25,413,113,25,25,"S",0,0,"default",Gold_img_set)

# 좌표지정
#hit_w = width - hit_x
#hit_h = height - hit_y

sheep = world.Wall(0,250,50,50,0,250,50,50,"S",0,0,"right",Sheep_img_set)
tree1 = world.Wall(100,300,50,150,100,400,50,50,"S",0,0,"default",Tree_img_set)
tree2 = world.Wall(200,300,50,150,200,400,50,50,"S",0,0,"default",Tree_img_set)
tree3 = world.Wall(400,200,50,150,400,300,50,50,"S",0,0,"default",Tree_img_set)
castle = world.Wall(100,100,100,100,100,100,100,100,"S",0,0,"default",Castle_img_set)
house = world.Wall(250,50,50,100,250,100,50,50,"S",0,0,"default",House_img_set)
tower = world.Wall(300,200,50,150,300,300,50,50,"S",0,0,"default",Tower_img_set)




warrior_draw = DrawImage(warrior)
castle_draw = DrawImage(castle)
house_draw = DrawImage(house)
tower_draw = DrawImage(tower)
gem_draw = DrawImage(gem)
gold_draw = DrawImage(gold)
tree1_draw = DrawImage(tree1)
tree2_draw = DrawImage(tree2)
tree3_draw = DrawImage(tree3)
sheep_draw = DrawImage(sheep)

background = world.Background(0,0,500,500,0,0,0,0,"S",0,0,"default",background_img_set)
background_draw = DrawImage(background)

# hitbox수정필요!
World_Walls = [sheep,tree1,tree2,tree3,castle,house,tower]
world_Items = [gem,gold]
World_objects_draw=[(background,background_draw),
                    (warrior,warrior_draw),
                    (sheep,sheep_draw),
                    (tree1,tree1_draw),
                    (tree2,tree2_draw),
                    (tree3,tree3_draw),
                    (castle,castle_draw),
                    (house,house_draw),
                    (tower,tower_draw),
                    (gem,gem_draw),
                    (gold,gold_draw)]


Item_count = 0

#warrior.set_state("left")
#warrior.set_velocity(6,1)
#warrior.set_direction("R")
sheep.set_velocity(4,0)
sheep.set_direction("R")
sheep.move_left_right(500)
#warrior.set_velocity(2,1)
ratValue = 0
def frame_loop(*args):
    global lastTime
    global warrior_draw
    global warrior
    global castle
    global ratValue
    global Item_count
    global World_objects_draw
    #print(lastTime)
    
    
    if lastTime%3 ==0:
        
        ctx.clearRect(0, 0, canvas.width, canvas.height)
        sheep.move_left_right(500)
        #ctx.clearRect(0, 0, canvas.width, canvas.height)
        
        # 그리는 부분 수정!
        for obj,draw in World_objects_draw:
            update_draw(obj,draw)
        
        for wall in World_Walls:
            if warrior.check_collision(wall):                                                                                                                    
                warrior.set_velocity(0,0)
        window.sendXY(warrior.x,warrior.y)
        
        for item in world_Items:
            if warrior.check_collision(item):
                Item_count += 1
                world_Items.remove(item)
                #console.log(Item_count)
                World_objects_draw = [pair for pair in World_objects_draw if pair[0].id != item.id]
                #notify_server_game_completed()
                
                if Item_count == 2:
                    notify_server_game_completed()
                
        if check_out(warrior):
            warrior.set_velocity(0,0)
        UserLoopCode()
        
    lastTime = lastTime+1 if lastTime <= float('inf') else 0    
    ratValue = window.requestAnimationFrame(create_proxy(frame_loop))
    
    
    #ctx.clearRect(0, 0, canvas.width, canvas.height)   
    #update_draw(rabbit,rabbit_draw)
    
    #window.requestAnimationFrame(create_proxy(frame_loop))


def controls(e):
    global warrior
    warrior.set_velocity(10,10)
    if e.code == 'KeyW':
        warrior.set_direction("U")
    elif e.code =='KeyS':
        warrior.set_direction("D")
    elif e.code == 'KeyA':
        warrior.set_direction("L")
        warrior.set_state("left")
    elif e.code == 'KeyD':
        warrior.set_direction("R")
        warrior.set_state("right")
        
document.addEventListener('keydown',create_proxy(controls))

frame_loop()
UserInitCode()




# => 시작함수 처음 시작할때만 작동합니다! => run으로 시작!
# => 반복함수 게임이 진행되는 동안 계속 작동합니다.
#=> 부분 나누기!