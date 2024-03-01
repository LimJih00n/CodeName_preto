class GameObject:
    _id_counter = 0
    
    def __init__(self, x, y, w, h,hit_x,hit_y,hit_w,hit_h,direction, dx, dy,state,img_set):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.direction = direction
        self.dx = dx
        self.dy = dy
        self.state = state
        self.img_set = img_set
        self.hit_x = hit_x
        self.hit_y = hit_y
        self.hit_w = hit_w
        self.hit_h = hit_h
        self.id = GameObject._id_counter  # 객체별 유니크 ID 할당
        GameObject._id_counter += 1
        #self.image.src = image_src

    #init정리필요!
    def update_position(self):
        if self.direction == 'U':
            self.hit_y -= self.dy
            self.y -= self.dy
        elif self.direction == 'D':
            self.hit_y += self.dy
            self.y += self.dy
        elif self.direction == 'R':
            self.hit_x += self.dx
            self.x += self.dx
        elif self.direction == 'L':
            self.hit_x -= self.dx
            self.x -= self.dx
        elif self.direction == 'S':
            pass  # 정지 상태
    
    def set_direction(self,dir):
        self.direction = dir
        
    def set_velocity(self,dx,dy):
        self.dx = dx
        self.dy = dy
    
    def set_state(self,state):
        self.state = state
    
    def turn_left(self):
        direction_order = ['U', 'L', 'D', 'R']
        current_index = direction_order.index(self.direction)
        self.direction = direction_order[(current_index + 1) % 4]

    def turn_right(self):
        direction_order = ['U', 'R', 'D', 'L']
        current_index = direction_order.index(self.direction)
        self.direction = direction_order[(current_index + 1) % 4]
        
    #def check_collision(self, obj):
        #if (self.x <= obj.x <= self.x+self.hit_w)or(self.x <=obj.x+obj.hit_w<=self.x+self.hit_w)or(self.y <= obj.y <= self.y+self.hit_h)or(self.y<=obj.y+obj.hit_h<=self.y+self.hit_h):
         #   return True
        #return False
    def check_collision(self, other):
    # A의 오른쪽 경계가 B의 왼쪽 경계보다 오른쪽에 있는지 확인
        right_of_other_left = self.hit_w + self.hit_x >  other.hit_x
        # A의 왼쪽 경계가 B의 오른쪽 경계보다 왼쪽에 있는지 확인
        left_of_other_right = self.hit_x <  other.hit_w + other.hit_x
        # A의 하단 경계가 B의 상단 경계보다 아래에 있는지 확인
        below_other_top = self.hit_h + self.hit_y > other.hit_y
        # A의 상단 경계가 B의 하단 경계보다 위에 있는지 확인
        above_other_bottom =  self.hit_y <  other.hit_h + other.hit_y
        

        # 모든 조건이 참이면 충돌 발생
        if right_of_other_left and left_of_other_right and below_other_top and above_other_bottom:
            return True
        else:
            return False

        

class Hero(GameObject):
    def __init__(self, x, y, w, h,hit_x,hit_y,hit_w,hit_h, direction='S', dx=0, dy=0,state="default",img_set={}):
        super().__init__(x, y, w, h,hit_x,hit_y,hit_w,hit_h,direction, dx, dy,state,img_set)

class Wall(GameObject):
    def __init__(self, x, y, w, h,hit_x,hit_y,hit_w,hit_h, direction='S', dx=0, dy=0,state="default",img_set={}):
        super().__init__(x, y, w, h,hit_x,hit_y,hit_w,hit_h,direction, dx, dy,state,img_set)
    
    def move_left_right(self,X):
        if self.x > X-self.width and self.state == "right":
            self.direction = "L"
            self.state = "left"
        elif self.x<0 and self.state =="left":
            self.direction = "R"
            self.state ="right"
        
            
        

class Background(GameObject):
    def __init__(self, x, y, w, h,hit_x=0,hit_y=0,hit_w=0,hit_h=0, direction='S', dx=0, dy=0,state="default",img_set={}):
        super().__init__(x, y, w, h,hit_x,hit_y,hit_w,hit_h,direction, dx, dy,state,img_set)



class Item(GameObject):
    def __init__(self, x, y, w, h,hit_x,hit_y,hit_w,hit_h, direction='S', dx=0, dy=0,state="default",img_set={}):
        super().__init__(x, y, w, h,hit_x,hit_y,hit_w,hit_h,direction, dx, dy,state,img_set)
        
class Monster(GameObject):
    def __init__(self, x, y, w, h,hit_x,hit_y,hit_w,hit_h, direction='S', dx=0, dy=0,state="default",img_set={}):
        super().__init__(x, y, w, h,hit_x,hit_y,hit_w,hit_h,direction, dx, dy,state,img_set)


