#!/usr/bin/env python3
# ##################################################################
#
# CSSE1001/7030 - Assignment 3
#
#   Student Username: s4261634
#
#   Student Name: Joshua Bitossi
#
#   Version: 1.0.1
#
###################################################################

###################################################################
#
# The following is support code. DO NOT CHANGE.

from assign3_support import *


# End of support code
################################################################
# Write your code below
################################################################

# Write your classes here (and import statements, i.e. tkinter)
import tkinter as tk
from tkinter import messagebox
from tkinter import font


### TO DO ###
# Should points variable be in model of tkinter class?
# What is step_ball doing?

class Model(object):
    """
    Manages all of the data.

    """

    def __init__(self, level_data):
        """
    """
        self._timer = 0
        self._block_dict = {}
        self._wall_dict = {}
        self._lives = 3             # Number of 'balls' the player has
        self._level = level_data
        self._grid = GridInfo()
        self._points = 10

        self._paddle = Paddle(100)
        self._ball = Ball(100,100)

        self.set_ball_speed(10,10)

    def update(self):
        """ Updates the model. Runs in increments of TIME_STEP.

        Model.update() -> None
        """

        # Update ball position
        # Get current position of ball
        ballx, bally = self.get_ball_position()
        # Get current speed of ball
        ballsx, ballsy = self.get_ball_speed()
        # INcrement current position by ball's speed
        self.set_ball_position((ballx+ballsx),(bally+ballsy))


    def load_level(self):
        """ Loads level information (blocks, etc) into the model from the levelfile corresponding to the filename.

        Model.load_level(dict) -> None
        """

        # Load json file
        level_info = read_level_data(self._level)

        # Read and set length of timer
        self._timer = level_info['timer']   # Set timer count

        # Set Blocks
        for n in level_info['blocks']:
            block_image = n[1]['image']         # Get block image
            block_can_delete = n[1]['delete']   # Can block be deleted?
            block_points = n[1]['points']       # How many points for hitting?
            position = n[0]                     # Block position

            # Add block instance to dictionary
            block_dictionary = {(position[0],position[1]):{"image":block_image,
            "delete":block_can_delete,
            "points": block_points}}

            # Add dictionary of block instance to dictionary of blocks
            self._block_dict.update(block_dictionary)

        # For each block in block_dict create a Block instance
        for block in self._block_dict:
            b = self._block_dict[block]
            Block(b['image'],b['delete'],b['points'])


    def get_ball_position(self):
        """ Returns the position of the ball as an (x, y) pair.

        Model.get_ball_position() -> (int, int)
        """
        return self._ball.get_position();

    def get_ball_speed(self):
        """ Returns the speed of the ball as an (xspeed, yspeed) pair.

        Model.get_ball_speed() -> (int, int)
        """
        return self._ball.get_speed();

    def set_points(self, points):
        """ Increments number of points in the model by points.
        Model.set_points(int) -> None
        """
        self._points += points

    def get_points(self):
        """ Returns the number of points player has.

        Model.get_points() -> int
        """
        return self._points

    def set_ball_position(self, x, y):
        """ Sets the position of the ball to (x, y).

        Model.set_ball_position(int, int) -> None
        """
        self._ball.set_position(x,y)

    def set_ball_speed(self, xspeed, yspeed):
        """ Sets the speed of the ball to (xpeed, yspeed).

        Model.set_ball_position(int, int) -> None
        """
        self._ball.set_speed(xspeed, yspeed)


    def is_block_at(self,cell_pos):
        """ This method returns true if there is a block at cell position
        cell_pos( row, column pairs)

        Model.is_block_at([int, int]) -> bool
        """

        if cell_pos in self._block_dict:
            return True
        else:
            return False

    def get_paddle_box(self):
        """ Returns paddle box from Paddle.get_box().

        Model.get_paddle_box() -> (int, int, int, int)
        """
        return self._paddle.get_box();

    def exit_ball(self):
        """ Used to tell the model that the ball has got passed the paddle.

        Model.step_ball() -> bool
        """
        ball_position = self.get_ball_position()    # Get position of ball
        paddle_box = self.get_paddle_box()          # Get position of paddle

        if ball_position[0] < paddle_box[0]:
            return True
        else:
            return False

    def step_ball(self):
        """ step ball"""
        current_position = self.get_ball_position()
        speed = self.get_ball_speed()
        new_x = current_position[0] + speed[0]
        new_y = current_position[1] + speed[1]
        self.set_ball_position(new_x,new_y)

class Block(object):
    """
    Represents a block.
    """

    def __init__(self, image, can_delete, points):
        self._block_image = image      # Name of block image
        self._can_delete = can_delete     # Can the block be removed by ball?
        self._points = points            # Points of rewarded for removing the block


    def get_image(self):
        """ Returns name of block image.

        BLock.get_image() -> str
        """
        return self._block_image

    def can_delete(self):
        """Returns whether the block can be deleted or not.
        Block.can_delete() -> bool
	    """
        return self._can_delete


    def get_points(self):
        """ Returns number of points obtained by hitting the block.

        Block.get_points() -> int
        """
        return self._points

    def __repr__(self):
        """ String representation of block.
        """

        return str(self.get_image()+" "+str(self.can_delete())+" "+str(self.get_points()))


class Paddle(object):
    """
	Represents a paddle
	"""

    def __init__(self, x_position):
        """ Constructor for Paddle class.eg Paddle(200)
	    """
        self._x = x_position
        self._halfw = BLOCK_WIDTH / 2   # Half paddle height
        self._halfh = PADDLE_HEIGHT / 2     # Half block width

    def get_centre(self):
        """ Returns x, y co-ordinates of paddle centre.

	    get_centre -> (int, int)
	    """

        return self._x,int(HEIGHT-(PADDLE_HEIGHT/2)) #Paddle is always along the bottom

    def get_box(self):
        """ Returns position of each corner of the box

	    get_box() -> (int, int, int, int)
	    """

        gc = self.get_centre()
        return int(gc[0]-self._halfw),\
        int(gc[1]-self._halfh),\
        int(gc[0]+self._halfw),\
        int(gc[1]+self._halfh)

    def move(self, position):
        """ Moves the paddle to 'position'

	    move(int) -> None
	    """

        # Make sure the paddle stays on the screen
        if position <= (0+self._halfw):
            self._x = 0+self._halfw
        elif position > WIDTH-self._halfw:
            self._x = WIDTH-self._halfw
        else:
            self._x = position

class Ball(object):
    """
    Representation of ball.
    """

    def __init__(self, x, y):
        """ Constructor for ball instance. Initiates ball at position (x,y).
	assign3.py"""
        self._x = x
        self._y = y
        self._speedx = 0
        self._speedy = 0

    def get_position(self):
        """ Returns current position of ball.

        get_position() -> (int, int)
        """
        return (self._x, self._y)

    def set_position(self, x, y):
        """ Sets position of ball to position (x, y).

        set_position(int, int) -> None
	    """

        self._x = x
        self._y = y

    def get_speed(self):
        """ Returns current vertical and horizontal speed of ball.

        get_speed() -> (int, int)
	    """

        return (self._speedx,self._speedy)

    def set_speed(self, x, y):
        """ Sets the vertical and horizontal speed of the ball.

	    set_speed(int, int) -> None
	    """

        self._speedx = x
        self._speedy = y

    def set_x_position(self, x):
        """ Sets the horizontal position of the ball. Used when ball is 'stuck' to the paddle and paddle is moved.

	    set_x_position(int) -> None
	    """

        self._x = x

class StatusEG(tk.Frame):
    def __init__(self, master, parent):
        super().__init__(master)

        self._ball_list = []

        # Create a font
        self.customFont = font.Font(family="Helvetica", size=20)

        # Create a label using the font
        self.points= tk.Label(self, text=0, width = 10, font = self.customFont)

        # Pack Label
        self.points.pack(side=tk.TOP, fill=tk.X)

        # Assign image file to ball_image
        self.ball_image = tk.PhotoImage(file = 'ball.gif')


    def update_balls(self, lives):
        """ Updates number of balls shown to number of items in self._ball_list.

        update_lives() -> None
        """

        for i in range(lives):
            self._ball_list.append(tk.Label(self, image = self.ball_image))
            self._ball_list[i].pack(side=tk.RIGHT)

    def update_label(self, value):
        """Used to update the points label.

        update_label(int) -> None
        """
        self.points.configure(text="{0}".format(value))

    def remove_ball_label(self):
        """ Removes one ball from lives.

        remove_ball_label() -> None
        """
        self.ball_label.pack_forget()

class Breakout(object):
    def __init__(self, master):
        master.title("Breakout")
        self._master = master

        # Create grid
        self.grid = GridInfo()

        # Create the model
        self.model = Model('level1.json')
        self.model.load_level()

        # Collision Handler
        self.collisions = CollisionHandler(self.model)

        # Status bar
        self.status_bar = StatusEG(master, self)
        self.status_bar.pack(expand=1, fill=tk.X, padx=20)

        # Create canvas
        self._canvas = tk.Canvas(master, bg='grey60', width=WIDTH, height=HEIGHT)
        self._canvas.config(scrollregion=[0,0,0,0])
        self._canvas.pack(expand=1, padx=20, pady=20)

        # Bind the leave and enter events for the canvas
        self._canvas.bind("<Leave>", self.leave)
        self._canvas.bind("<Enter>", self.enter)

        # Turn the cursor off when in the canvas
        self._canvas['cursor'] = "none"

        # Track mouse movement
        self._canvas.bind("<Motion>",self.movement)

        # Create image objects from file
        self.images = {
            "ball.gif" : tk.PhotoImage(file = "ball.gif"),
            "red.gif" : tk.PhotoImage(file = "red.gif")
        }

        self.show()

        # Call when mouse is clicked
        self._master.after(TIME_STEP, self.update_game)

    def update_game(self):


        #Detect Collisions
        c = self.collisions.process_collisions()
        if len(c) > 0:
            for n in range(len(c)):
                if c[n] in self.model._block_dict:
                    if self.model._block_dict.get(c[n])['delete'] == True:
                        self.model.set_points(self.model._block_dict.get(c[n])['points'])
                        self.model._block_dict.pop(c[n])

        self.show()
        self.model.update()

        # Update status bar points
        self.status_bar.update_label(self.model.get_points())

        # Update status bar lives
        self.status_bar.update_balls(20)

        self._master.after(TIME_STEP, self.update_game)

    def show(self):
        self._canvas.delete(tk.ALL)

        # Paddle
        self.paddle = self._canvas.create_rectangle(self.model._paddle.get_box(),fill='blue',tags="<Paddle>")

        # Ball
        self.ball = self._canvas.create_image(self.model.get_ball_position(),image=self.images["ball.gif"],tags="<Ball>")

        # Create blocks
        for n in self.model._block_dict:
            x = (int(n[0]) * BLOCK_HEIGHT)
            y = (int(n[1]) * BLOCK_WIDTH)-BLOCK_WIDTH/2# fix by using gridinfo(?)
            self._canvas.create_image(y, x,image=self.images['red.gif'])


        # Create walls (Have to do in show and not load_level because all blocks
        # are deleted each step)
        # Top
        for n in range(NUM_COLUMNS+2):
            self.model._block_dict.update({(0, n):{'image': 'red.gif','delete': False, 'points': 0}})
        # Right
        for n in range(0,NUM_ROWS+2):
            self.model._block_dict.update({(n,NUM_COLUMNS+1):{'image': 'red.gif','delete': False, 'points': 0}})
        # Bottom
        for n in range(NUM_ROWS+2):
            self.model._block_dict.update({(n, NUM_COLUMNS+1):{'image': 'red.gif','delete': False, 'points': 0}})
        # Left
        for n in range(NUM_ROWS+2):
            self.model._block_dict.update({(n, 0):{'image': 'red.gif','delete': False, 'points': 0}})


    def movement(self, event):

        self.model._paddle.move(event.x)
        new_x = self.model._paddle.get_box()
        self._canvas.coords("<Paddle>",new_x,)

    def walls_list(self):
        top = []
        right = []
        bottom = []
        left = []
        # Top
        for n in range(NUM_COLUMNS+2):
            top.append([n,0])

        # Right
        for n in range(NUM_ROWS+2):
            right.append([NUM_COLUMNS+1,n])

        # Bottom
        for n in range(NUM_COLUMNS+2):
            bottom.append([NUM_ROWS+1,n])

        # Left
        for n in range(NUM_ROWS+2):
            left.append([n,NUM_COLUMNS+1])

        combined = top+right+bottom+left
        return combined


    def leave(self, e):
        print("Leaving canvas")

    def enter(self, e):
        print("Entering canvas")


def main():
    # # Write your GUI instantiation code here
    root = tk.Tk()
    app = Breakout(root)
    root.mainloop()


################################################################
# Write your code above - NOTE you should define a top-level
# class (the application) called Breakout
################################################################
if __name__ == '__main__':
    main()
