from circleshape import *
from constants import *


class Shot(CircleShape):
    def __init__(self,x:float,y:float,radius:float)->None:
        super().__init__(x,y,radius)
        self.x=x
        self.y=y
        self.radius=radius

    def draw(self,screen):
        circle=pygame.draw.circle(screen,"White",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position+=self.velocity*dt
            