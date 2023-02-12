from model import Model
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from PIL import ImageGrab
from pyscreenshot import grab
import tkinter as tk
import numpy as np

#window
root = Tk()
root.title('White Board')
root.geometry('1350x670+150+50')
root.configure(bg='#f2f3f5')
root.resizable(False, False)

current_x = 0
current_y = 0
color = 'white'
def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x, current_y
    canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(), fill=color
    , capstyle=ROUND, smooth=True)
    current_x, current_y = work.x, work.y

def show_color(new_col):
    global color
    color = new_col

def new_canvas():
    canvas.delete('all')
    display_pallete()

#window icon
image_icon = PhotoImage(file='assets/images/logo.png')
root.iconphoto(False, image_icon)

#create a color_box that contains a color canvas(colors pallette)
color_box_image = PhotoImage(file='assets/images/color section.png')
Label(root, image=color_box_image, bg='#f2f3f5').place(x=10, y=20)

colors = Canvas(root, bg='#ffffff', width=37, height=300, bd=0)
colors.place(x=30, y=60)

eraser = PhotoImage(file='assets/images/eraser.png')
Button(root, image=eraser, bg='#f2f3f5', command=new_canvas).place(x=30, y=400)

#Drawing area
canvas = Canvas(root, bg='#000000', width=1230, height=600, cursor='hand2')
canvas.place(x=100, y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)


def display_pallete():
    id = colors.create_rectangle((10, 10, 30, 30), fill='white')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('white'))
    
    id = colors.create_rectangle((10, 40, 30, 60), fill='gray')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))
    
    id = colors.create_rectangle((10, 70, 30, 90), fill='brown4')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))
    
    id = colors.create_rectangle((10, 100, 30, 120), fill='red')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))
    
    id = colors.create_rectangle((10, 130, 30, 150), fill='orange')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))
    
    id = colors.create_rectangle((10, 160, 30, 180), fill='yellow')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))
    
    id = colors.create_rectangle((10, 190, 30, 210), fill='green')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))
    
    id = colors.create_rectangle((10, 220, 30, 240), fill='blue')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))
display_pallete()

#slider
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(max(50, current_value.get()))

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root, from_=50, to=100, orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=130, y=630)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=127, y=650)

def predict():
    global result
    x1 = root.winfo_x() + canvas.winfo_x() + 180
    y1 = root.winfo_y() + canvas.winfo_y() + 90
    x2 = x1 + canvas.winfo_width() + 76
    y2 = y1 + canvas.winfo_height() + 58
    coordinates = (x1, y1, x2, y2)
    i = grab(bbox=coordinates)
    
    i = i.resize((28, 28))
    i = i.convert('L')
    #i.show()
    i = np.array(i)
    
    model = Model()
    pred = model.predict(i)
    
    result.config(text = 'Result: '+str(pred))

button = Button(text='Predict', command=predict)
button.place(x=1280, y=630)

#Result
result = ttk.Label(root, text='')
result.place(x=700, y=630)


root.mainloop()
