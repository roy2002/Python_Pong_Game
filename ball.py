import turtle


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x = 10
        self.y = 10

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_r(self):
        self.y *= -1

    def bounce_l(self):
        self.x *= -1

    def bounce_paddle(self):
        self.y *= -1
        self.x *= -1







