# Patrik Valach
# 03.11.2021

import tkinter 
import random

farba = ['black', 'gray', 'brown', 'red', 'orange', 'yellow', 'green', 'lightblue', 'blue', 'purple', 'white']
xy=[]
color_buttons = []
farba_set = 'black'
width_entry = ''

def reset_controls():
    # reset controls
    global xy
    c.focus_set()
    c.unbind('<Button-1>')
    c.unbind('<B1-Motion>')
    c.unbind('<ButtonRelease-1>')
    xy = []
# ---------------Line Draw---------------------------------
def line_draw_cntrl():
    reset_controls()
    c.bind('<Button-1>', click)
    c.bind('<B1-Motion>', move)
    c.bind('<ButtonRelease-1>', release)

def click(event):
    global x, y
    x,y = event.x, event.y
    c.focus_set()

def move(event):
    global x, y, hrubka, farba, farba_cislo
    release(None)
    c.create_line(x,y,event.x,event.y, width=width_var.get(), fill=farba_set, capstyle=tkinter.ROUND)
    click(event)

def release(event):
    global  farba_cislo
    if not width_var.get().isdigit():
        width_var.set('1')
# ------------------------------------------------

# ------------Rectangle------------------------------------
def rect_draw(event):
    global xy
    c.focus_set()
    xy += [event.x, event.y]
    if len(xy) == 4:
        c.create_rectangle(xy, fill=farba_set)
        xy = []

def rect_draw_cntrl():
    reset_controls()
    c.bind('<Button-1>', rect_draw)
# ------------------------------------------------

# --------------Oval----------------------------------
def oval_draw(event):
    global xy
    c.focus_set()
    xy += [event.x, event.y]
    if len(xy) == 4:
        c.create_oval(xy, fill=farba_set)
        xy = []

def oval_draw_cntrl():
    reset_controls()
    c.bind('<Button-1>', oval_draw)
# ------------------------------------------------

# --------------Triangle----------------------------------
def tri_draw(event):
    global xy
    c.focus_set()
    xy += [event.x, event.y]
    if len(xy) == 6:
        c.create_polygon(xy, fill=farba_set)
        xy = []

def tri_draw_cntrl():
    reset_controls()
    c.bind('<Button-1>', tri_draw)
# ------------------------------------------------

# -------------------Polygon-----------------------------
def poly_draw(event):
    global xy
    c.focus_set()
    if not poly_num.get().isdigit():
        poly_num.set('5')
    elif int(poly_num.get()) < 2:
        poly_num.set('5')
    xy += [event.x, event.y]
    if len(xy) == int(poly_num.get()) * 2:
        c.create_polygon(xy, fill=farba_set)
        xy = []

def poly_draw_cntrl():
    reset_controls()
    c.bind('<Button-1>', poly_draw)
# ------------------------------------------------

# ----------------Color--------------------------------
def set_clr(farba):
    global farba_set
    c.focus_set()
    farba_set = farba
# ------------------------------------------------

# Main Window
root = tkinter.Tk()
root.title('paint')
root['bg'] = 'light grey'

# Canvas
c = tkinter.Canvas(width=640, height=480, bd=2)
c.grid(row=0, column=0)

# Width input
width_lbl = tkinter.Label(root, text='Width:', bg='light grey')
width_lbl.grid(row=1, column=0, sticky='e', padx=130)
width_var = tkinter.StringVar(root, '1')
width_entry = tkinter.Entry(root, textvariable=width_var)
width_entry.grid(row=1, column=0, sticky='e')

# Polygon input
poly_num = tkinter.StringVar(root, '5')
poly_entr = tkinter.Entry(root, textvariable=poly_num)
poly_entr.grid(row=5, column=0, sticky='e')
poly_lbl = tkinter.Label(root, text='Num of Vertexes:', bg='light grey').grid(row=5, column=0, sticky='e', padx=130)

# -----------------Buttons for Different Shapes--------------
btn_clear = tkinter.Button(root, text='Clean Canvas', command=lambda: c.delete('all'),width = 13)
btn_clear.grid(row=0, column=1, sticky='s')

btn_draw = tkinter.Button(root, text='Line Draw', command=lambda: line_draw_cntrl(),width = 13)
btn_draw.grid(row=1, column=1)

btn_rect = tkinter.Button(root, text='Rectangle Draw', command=lambda: rect_draw_cntrl(),width = 13)
btn_rect.grid(row=2, column=1)

btn_oval = tkinter.Button(root, text='Oval Draw', command=lambda: oval_draw_cntrl(),width = 13)
btn_oval.grid(row=3, column=1)

btn_tri = tkinter.Button(root, text='Triangle Draw', command=lambda: tri_draw_cntrl(),width = 13)
btn_tri.grid(row=4, column=1)

btn_poly = tkinter.Button(root, text='Polygon Draw', command=lambda: poly_draw_cntrl(),width = 13)
btn_poly.grid(row=5, column=1)


# -----------------------------------------------------------------

btn_end = tkinter.Button(root, text='Exit', command=lambda: root.destroy(),width = 10, height=5, bg='grey')
btn_end.grid(row=0, column=4, sticky='n', pady=5)

release(None)

# Color Buttons
for i in range(len(farba)):
    def color_picker(i):
        color_buttons.append(tkinter.Button(root, text=farba[i], bg=farba[i], command=lambda: set_clr(farba[i]),width = 10))
        color_buttons[i].grid(row=i+1-i//4*4, column=2+i//4)
        if farba[i] == 'black':
            color_buttons[i]['fg'] = 'white'
    color_picker(i)

c.focus_set()
root.mainloop()