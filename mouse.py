import math
import turtle
from turtle import Turtle

window = turtle.Screen()
window.bgcolor("black")
window.setup(700, 700)

turtle.register_shape("mouse_left.gif")
turtle.register_shape("mouse_right.gif")


class Player(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape('mouse_right.gif')
        self.color('blue')
        self.penup()
        self.speed(0)
        self.cheese = 0

    def go_jump(self, pipes, player):
        self.speed(3)
        if self.heading() == 0:
            move_to_x = player.xcor() + 22
            move_to_y = player.ycor() + 22
            if (move_to_x, move_to_y) not in pipes and (self.xcor(), self.ycor() + 22) not in pipes:
                self.goto(move_to_x, move_to_y)
        if self.heading() == 180:
            move_to_x = player.xcor() - 22
            move_to_y = player.ycor() + 22
            if (move_to_x, move_to_y) not in pipes and (self.xcor(), self.ycor() + 22) not in pipes:
                self.goto(move_to_x, move_to_y)
        while (self.xcor(), self.ycor() - 22) not in pipes:
            self.goto(self.xcor(), self.ycor() - 22)
        self.speed(3)

    def go_highjump(self, pipes, player):
        self.speed(3)
        if self.heading() == 0:
            move_to_x = player.xcor() + 22
            move_to_y = player.ycor() + 66
            if (move_to_x, move_to_y) not in pipes and (self.xcor(), self.ycor() + 22) not in pipes and (
                    self.xcor(), self.ycor() + 44) not in pipes and (self.xcor(), self.ycor() + 66) not in pipes:
                self.goto(move_to_x, move_to_y)
        self.speed(3)
        if self.heading() == 180:
            move_to_x = player.xcor() - 22
            move_to_y = player.ycor() + 66
            if (move_to_x, move_to_y) not in pipes and (self.xcor(), self.ycor() + 22) not in pipes and (
                    self.xcor(), self.ycor() + 44) not in pipes and (self.xcor(), self.ycor() + 66) not in pipes:
                self.goto(move_to_x, move_to_y)
        while (self.xcor(), self.ycor() - 22) not in pipes:
            self.goto(self.xcor(), self.ycor() - 22)
        self.speed(3)

    def go_left(self, pipes, player):
        self.shape('mouse_left.gif')
        move_to_x = player.xcor() - 22
        move_to_y = player.ycor()
        self.setheading(180)
        if (move_to_x, move_to_y) not in pipes:
            self.goto(move_to_x, move_to_y)
            if (move_to_x, move_to_y - 22) not in pipes:
                self.goto(move_to_x, move_to_y)
        while True:
            if (self.xcor(), self.ycor() - 22) not in pipes:
                self.goto(player.xcor(), self.ycor() - 22)
            else:
                break

    def go_right(self, pipes, player):
        self.shape('mouse_right.gif')
        move_to_x = player.xcor() + 22
        move_to_y = player.ycor()
        self.setheading(0)
        if (move_to_x, move_to_y) not in pipes and (move_to_x, move_to_y - 22) in pipes:
            self.goto(move_to_x, move_to_y)
        elif (move_to_x, move_to_y) not in pipes and (move_to_x, move_to_y - 22) not in pipes:
            self.goto(move_to_x, move_to_y - 22)
        while True:
            if (self.xcor(), self.ycor() - 22) not in pipes:
                self.goto(player.xcor(), self.ycor() - 22)
            else:
                break

    # check whether the mouse collides with another
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 5:
            return True
        else:
            return False

    def destroy(self):
        self.goto(1000, 1000)
        self.hideturtle()
