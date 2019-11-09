from arcade import Sprite
from math import sin,cos, radians

class Player (Sprite):
    def __init__(self, x, y, name, colour):
        super().__init__(

            "images/PNG/playerShip1_blue.png"
        )
        self.center_x = x
        self.center_y = y
        self.name = name

    
    def turn_left(self):

        self.angle = self.angle + 1

    def turn_right(self):

        self.angle = self.angle - 1

    def move_forward(self):
        # pi/180
        angleinradians = radians(self.angle)
        self.center_x = self.center_x + (cos(angleinradians)*5)
        self.center_y = self.center_y + (sin(angleinradians)*5)

    def move_backward(self):


