from turtle import Turtle
WIDTH = 5
HEIGHT = 1
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.setposition(x_pos, y_pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

