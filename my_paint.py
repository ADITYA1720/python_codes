#Author: shriaas2898
'''This program contains code to create paint like application.
   The code is based on an article  "How to make paint in python" published on papaprogrammer.com
   with some added features.
'''
from tkinter import *
from tkinter.colorchooser import askcolor


# class paint
class Paint(object):
    DEFAULT_PEN_SIZE = 0.5
    DEFAULT_COLOR = "black"

    # initializing buttons
    def __init__(self):
        self.root = Tk()
        pen_image = PhotoImage(r'/home/shriaas/PycharmProjects/Desktop Apps/Icons/pen.svg').subsample(100,100)
        self.pen_button = Button(self.root, text="pen",
                                 image=pen_image,
                                 command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text="brush", command=self.use_brush)
        self.brush_button.grid(row=1, column=0)

        self.color_button = Button(self.root, text="color", command=self.choose_color)
        self.color_button.grid(row=2, column=0)

        self.eraser_button = Button(self.root, text="eraser", command=self.use_eraser)
        self.eraser_button.grid(row=3, column=0)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=4, column=0)

        self.canvas = Canvas(self.root, bg="white", width=600, height=600)
        self.canvas.grid(rowspan=5, column=1)

        self.setup()
        self.root.mainloop()

    # Function is triggered when pen button is clicked.
    def use_pen(self):
        self.activate_button(self.pen_button)

    # Function is triggered when brush button is clicked.
    def use_brush(self):
        self.activate_button(self.brush_button, brush_mode=True)

    # Lets user choose color from color palette
    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    # Function to activate eraser.
    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def setup(self):
        self.old_x = self.old_y = None
        self.line_width = self.DEFAULT_PEN_SIZE
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.brush_on = False
        self.active_button = self.pen_button
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    # Funtion to activate the button which is clicked
    def activate_button(self, button, eraser_mode=False, brush_mode=False):
        self.active_button.config(relief=RAISED)
        button.config(relief=SUNKEN)
        self.active_button = button
        self.eraser_on = eraser_mode
        self.brush_on = brush_mode

    # Function to paint on canvas with active brush/pen/eraser
    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color

        if self.old_x and self.old_y:
            if self.brush_on:
                self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                        width=self.line_width, fill=paint_color,
                                        capstyle=ROUND, smooth=True, splinesteps=36, stipple='gray25')
            else:
                self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                        width=self.line_width, fill=paint_color,
                                        capstyle=ROUND, smooth=True, splinesteps=36)

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        print("LOG: Reset ")

        self.old_x = self.old_y = None


if __name__ == '__main__':
    Paint()

