from turtle import Turtle


class Cheese(Turtle):
    def __init__(self, x, y, cheese=1):
        Turtle.__init__(self)
        self.shape('cheese2.gif')
        self.color('yellow')
        self.penup()
        self.speed(0)
        self.__cheese = cheese
        self.goto(x, y)

    @property
    def cheese(self):
        return self.__cheese

    @cheese.setter
    def cheese(self, cheese):
        self.__cheese = cheese

    def destroy(self):
        self.goto(1000, 1000)
        self.hideturtle()
