
from tkinter import *
import random
import time

tk = Tk()
tk.title('Catch Kirby!')
tk.wm_attributes('-topmost', 1)
main = Canvas(tk, width=500, height=500)
main.pack()
bg = PhotoImage(file='Cloudbg.gif')
main.create_image(0, 0, image=bg, anchor=NW)
tk.update()
time.sleep(1)

class Kirby:
    def __init__(self, main, Cloudbar, color):
        self.main = main
        self.Cloudbar = Cloudbar
        self.id = main.create_oval(0, 0, 25, 25, fill=color)
        startpoint = self.main.move(self.id, 250, 50)
        startdirection = [-4, -3, 3, 4]
        random.shuffle(startdirection)
        self.x = startdirection[0]
        self.y = startdirection[0]
        self.frameheight = self.main.winfo_height()
        self.framewidth = self.main.winfo_width()
        self.hit_bottom = False

    def hit_Cloudbar(self, position):
        Cloudbar_position = self.main.coords(self.Cloudbar.id)
        if position[2] >= Cloudbar_position[0] and position[0] <= Cloudbar_position[2]:
            if position[3] >= Cloudbar_position[1] and position[3] <= Cloudbar_position[3]:
                return True
            return False

    def draw(self):
        self.main.move(self.id, self.x, self.y)
        position = self.main.coords(self.id)
        if position[0] <=0:
            self.x = 3
        if position[1] <= 0:
            self.y = 3
        if position[2] >= self.framewidth:
            self.x = -3
        if position[3] >= self.frameheight:
            self.hit_bottom = True
        if self.hit_Cloudbar(position) == True:
            self.y = -3

class Cloudbar:
    def __init__(self, main, color):
        self.main = main
        self.id = main.create_rectangle(0, 0, 150, 10, fill=color)
        self.x = 0
        self.y = 0 
        startpoint = self.main.move(self.id, 175, 400)
        self.frameheight = self.main.winfo_height()
        self.framewidth = self.main.winfo_width()
        self.main.bind_all('<KeyPress-Right>', self.move_right)
        self.main.bind_all('<KeyPress-Left>', self.move_left)

    def draw(self):
        self.main.move(self.id, self.x, self.y)
        position = self.main.coords(self.id)
        if position[0] <= 0:
            self.x = 0
        elif position[2] >= self.framewidth:
            self.x = 0

    def move_left(self, evt):
            self.x = -3

    def move_right(self, evt):
            self.x = 3

Cloudbar = Cloudbar(main, 'skyblue')
Kirby = Kirby(main, Cloudbar, 'pink')

while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01) 

    if Kirby.hit_bottom == False:
        Kirby.draw()
        Cloudbar.draw()
     
    else:
       main.create_text(250, 250, text='You lost Kirby!', font=('Courier', 40), fill='blue')
       break
