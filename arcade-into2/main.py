from arcade import * #import "everything"
from random import choice, randint
from player import Player

#similar to public static ___ in java
class Window(Window):
    def __init__(self):
        #super -> tell the class in charge to run the __init__ function
        super().__init__(1000, 1000, "my arcade window") #fullscreen = true
        #runs class meteor with the assigned parameters
        self.meteor = Meteor(200,200)
        # x2
        self.meteor2 = Meteor(200,200)
        #creates an empty list
        self.meteors = SpriteList()

        # 20x loop
        for i in range(20):
            #variable new meteor - set at a random position (randint)
            new_meteor = Meteor(randint(0,self.width),randint(0,self.height))
            #append - appends an item to a list
            self.meteors.append(new_meteor)
        print(self.meteors)
        
        self.player = Player(self.width/2, self.height/2, "armando", "blue")



    def on_draw(self):
        start_render()

        self.player.draw()
        draw_text("omg did this work", 0, self.height, color.LIGHT_BLUE, font_size = 40, font_name=('calibri'), anchor_y="top")
        self.meteor.draw()
        self.meteor2.draw()

        #len(list) - gets the length (number of items) of a list
        for i in range(len(self.meteors)):
            self.meteors[i].draw()
     

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_key_press(self, symbol, modifiers):

        if symbol == key.A or symbol == key.LEFT:
            self.player.turn_left()
        elif symbol == key.D or symbol == key.RIGHT:
            self.player.turn_right()
        else:
            randommeteor = choice(self.meteors)
            new_meteor = randommeteor.breakapart()
            if new_meteor:
                self.meteors.append(new_meteor)



class Meteor(Sprite):
    def __init__(self, x, y, colour=None, size = 4):
        super().__init__("images/PNG/Meteors/meteorGrey_big4.png", center_x=x, center_y=y,)

        if colour:
            #if the meteor is given a color use that color
            self.colour = colour
        else:
            #if not, choose at random
            self.colour = choice(["grey","brown"])

        self.size = size



        if self.colour == "grey":
            if self.size == 4:
                images = [
                    "images/PNG/Meteors/meteorGrey_big1.png",
                    "images/PNG/Meteors/meteorGrey_big2.png",
                    "images/PNG/Meteors/meteorGrey_big3.png",
                ]
                self.texture = load_texture(choice(images))

            elif self.size == 3:
                images = [
                    "images/PNG/Meteors/meteorGrey_med1.png",
                    "images/PNG/Meteors/meteorGrey_med2.png",
                ]
                self.texture = load_texture(choice(images))

            elif self.size == 2:
                images = [
                    "images/PNG/Meteors/meteorGrey_small1.png",
                    "images/PNG/Meteors/meteorGrey_small2.png",
                ]
                self.texture = load_texture(choice(images))

            elif self.size == 1:
                images = [
                    "images/PNG/Meteors/meteorGrey_tiny1.png",
                    "images/PNG/Meteors/meteorGrey_tiny2.png",
                ]
                self.texture = load_texture(choice(images))
        else:
            if self.size == 4:
                images = [
                    "images/PNG/Meteors/meteorBrown_big3.png",
                    "images/PNG/Meteors/meteorBrown_big1.png",
                    "images/PNG/Meteors/meteorBrown_big2.png"
                ]
                self.texture = load_texture(choice(images))

            elif self.size == 3:
                images = [
                    "images/PNG/Meteors/meteorBrown_med2.png",
                    "images/PNG/Meteors/meteorBrown_med1.png",
                ]
                self.texture = load_texture(choice(images))

            elif self.size == 2:
                images = [
                    "images/PNG/Meteors/meteorBrown_small2.png",
                    "images/PNG/Meteors/meteorBrown_small1.png",
                ]
                self.texture = load_texture(choice(images))

            elif self.size == 1:
                images = [
                    "images/PNG/Meteors/meteorBrown_tiny2.png",
                    "images/PNG/Meteors/meteorBrown_tiny1.png",
                ]
                self.texture = load_texture(choice(images))

    def breakapart(self):
        self.kill()

        if self.size > 1:
            meteor1 = Meteor(self.center_x, self.center_y, colour = self.colour, size = self.size - 1)
            return meteor1
        




Window()
run()
