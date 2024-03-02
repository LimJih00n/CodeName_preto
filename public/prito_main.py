from js import document, window, Image, console
import js
import world
from pyodide import create_proxy
import datetime as dt
import asyncio
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
        self.image.src = "!"
        self.x = obj.x
        self.y = obj.y
        self.height = obj.height
        self.width = obj.width
        self.state = "default"
        self.frame_idx = 0
        self.frame_length = 0
    
    
    def draw(self, obj):
        
        self.frame_length = obj.img_dic[obj.state]["frame"]
        frame_width = obj.img_dic[obj.state]["f-width"] / self.frame_length
        frame_height = obj.img_dic[obj.state]["f-height"]
        self.x = obj.x
        self.y = obj.y
        self.width = obj.width
        self.height = obj.height
        
        
        if self.image.src != "!" or self.state != obj.state:
            self.image.src = obj.img_dic[obj.state]["img-url"]
        self.state = obj.state
                
        if obj.img_dic[self.state]["frame"] == 1:
            ctx.drawImage(self.image, self.x, self.y, self.width, self.height)
        else:
            ctx.drawImage(
            self.image, 
            self.frame_idx * frame_width, 0, # 스프라이트 시트에서의 x, y 위치
            frame_width-90, frame_height,    # 추출할 프레임의 너비와 높이
            self.x,self.y,                         # 캔버스 상의 x, y 위치
            self.width,self.height   # 캔버스 상의 프레임의 너비와 높이
            )
            self.frame_idx +=1
            self.frame_idx = (self.frame_idx + 1) % self.frame_length
        
        

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
#$user_init_out
def UserLoopCode():
    state=0
#$user_loop_start
    
#$user_loop_out


################################
knight_img_dic ={
    "default":
        {
            "frame":6,
            "f-width":1152,
            "f-height":100,
            "img-url": './assets/knight/right/w-right.png'
        },
    "left":{
            "frame":6,
            "f-width":1152,
            "f-height":100,
            "img-url": './assets/knight/left/w-left.png'
        },
    "right":{
            "frame":6,
            "f-width":1152,
            "f-height":100,
            "img-url": './assets/knight/right/w-right.png'
        }
}
sheep_img_dic = {
    "default":{
            "frame":6,
            "f-width":768,
            "f-height":60,
            "img-url": './assets/objects/sheep/right/sheep-right.png'
        },
    "right":{
            "frame":6,
            "f-width":768,
            "f-height":60,
            "img-url": './assets/objects/sheep/right/sheep-right.png'
        },
    "left":{
            "frame":6,
            "f-width":768,
            "f-height":60,
            "img-url": './assets/objects/sheep/left/sheep-left.png'
        },
}

tree_img_dic = {
    "default":{
            "frame":4,
            "f-width":768,
            "f-height":180,
            "img-url": './assets/objects/tree/Tree.png'
    }
}
goblin_img_dic = {
     "default":
        {
            "frame":6,
            "f-width":1152,
            "f-height":100,
            "img-url": './assets/goblin/right/g-right.png'
        },
    "left":{
            "frame":6,
            "f-width":1152,
            "f-height":100,
            "img-url": './assets/goblin/left/g-left.png'
        },
    "right":{
            "frame":6,
            "f-width":1152,
            "f-height":100,
            "img-url": './assets/goblin/right/g-right.png'
        }
}
Castle_img_dic = {
    "default":{
        "frame":1,
        "f-width":195,
        "f-height":288,
        "img-url":'./assets/Buildings/Castle/Castle_Blue.png'
    }
}
House_img_dic = {
      "default":{
        "frame":1,
        "f-width":108,
        "f-height":142,
        "img-url":'./assets/Buildings/House/House_Blue.png'
    }
}
Tower_img_dic ={
     "default":{
        "frame":1,
        "f-width":115,
        "f-height":173,
        "img-url":'./assets/Buildings/Tower/Tower_Blue.png'
    }
}
background_img_dic={
     "default":{
        "frame":1,
        "f-width":3300,
        "f-height":3300,
        "img-url":'./assets/background/grid_tile.png'
    }
}
gold_img_dic={
    "default":{
        "frame":7,
        "f-width":896,
        "f-height":80,
        "img-url":'./assets/objects/gold/G_Spawn.png'
    }
}

castle_set = []
World_Walls = []
#__init__(self, x, y, w, h,hit_x,hit_y,hit_w,hit_h,direction, dx, dy,state,img_set):

# hit box!
# 움직ㅇ리때 hit box도 움직여야함 
# 실제 자기 box 다름!
# hit x,y: hit box의 시작좌표
# hit_w _h : hit box의 width와 height

warrior = world.Hero(0,0,50,50,10,10,30,30,"S",0,0,"default",knight_img_dic)




# warrior: 1152-6: 192-100
#tree 768-4 -180
#sheep 768-6 - 60
#gold 896-7 - 80
#goblin 1152-6-100



gold = world.Item(413,113,25,25,413,113,25,25,"S",0,0,"default",gold_img_dic)

# 좌표지정
#hit_w = width - hit_x
#hit_h = height - hit_y

sheep = world.Wall(0,250,50,50,0,250,50,50,"S",0,0,"right",sheep_img_dic)
tree1 = world.Wall(100,300,50,150,100,400,50,50,"S",0,0,"default",tree_img_dic)
tree2 = world.Wall(200,300,50,150,200,400,50,50,"S",0,0,"default",tree_img_dic)
tree3 = world.Wall(400,200,50,150,400,300,50,50,"S",0,0,"default",tree_img_dic)
castle = world.Wall(100,100,100,100,100,100,100,100,"S",0,0,"default",Castle_img_dic)
house = world.Wall(250,50,50,100,250,100,50,50,"S",0,0,"default",House_img_dic)
tower = world.Wall(300,200,50,150,300,300,50,50,"S",0,0,"default",Tower_img_dic)



warrior_draw = DrawImage(warrior)
castle_draw = DrawImage(castle)
house_draw = DrawImage(house)
tower_draw = DrawImage(tower)
gold_draw = DrawImage(gold)
tree1_draw = DrawImage(tree1)
tree2_draw = DrawImage(tree2)
tree3_draw = DrawImage(tree3)
sheep_draw = DrawImage(sheep)

background = world.Background(0,0,500,500,0,0,0,0,"S",0,0,"default",background_img_dic)
background_draw = DrawImage(background)

# hitbox수정필요!
World_Walls = [sheep,tree1,tree2,tree3,castle,house,tower]
world_Items = [gold]
World_objects_draw=[(background,background_draw),
                    (warrior,warrior_draw),
                    (sheep,sheep_draw),
                    (tree1,tree1_draw),
                    (tree2,tree2_draw),
                    (tree3,tree3_draw),
                    (castle,castle_draw),
                    (house,house_draw),
                    (tower,tower_draw),
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
    
    
    if lastTime%8 ==0:
        
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