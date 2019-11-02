from arcade import Sprite


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
        pass

    def move_backward(self):
        pass

