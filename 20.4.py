from tkinter import *
import time
import random

WIDTH = 1024
HEIGHT = 720

tk = Tk()
cv = Canvas(tk, width = WIDTH, height = HEIGHT)
tk.title('Tkinter ballz')
cv.pack()


class Ball :
    def __init__(self, size, color) :
        self.shape = cv.create_oval(10, 10, size, size, fill = color)
        self.xspeed = random.randint(-10, 11)
        if self.xspeed == 0 :
            self.xspeed = random.randint(-10, 11)
        self.yspeed = random.randint(-10, 11)
        if self.yspeed == 0 :
            self.yspeed = random.randint(-10, 11)

    def move(self) :
        cv.move(self.shape, self.xspeed, self.yspeed)
        pos = cv.coords(self.shape)
        if pos [3] >= HEIGHT or pos [1] <= 0 :
            self.yspeed = -self.yspeed
            self.set_color(random.choice(colors))

        if pos [2] >= WIDTH or pos [0] <= 0 :
            self.xspeed = -self.xspeed
            self.set_color(random.choice(colors))

    def set_color(self, color) :
        cv.itemconfig(self.shape, fill = color)


colors = ['red', 'gold', 'orange', 'magenta', 'green', 'pink', 'cyan', 'black', 'grey', 'blue']
balls = []
for i in range(21) :
    balls.append(Ball(50, random.choice(colors)))

while True :
    for ball in balls :
        ball.move()
    tk.update()
    time.sleep(0.001)
