# In this script, you would finde the code of a simple calculator with the interface builded with the python library tkinter

from tkinter import *

window = Tk()
window.title("My Calculator")
i = 0

# calculator display:
display = Entry(window, font = "Helvetica 15")
display.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

def button_click(value):
    global i
    display.insert(i, value)
    i += 1

def delete():
    display.delete(0, END)
    i = 0

def result():
    expression = display.get()
    result = eval(expression)
    delete()
    display.insert(0, result)




# calculator buttons:
width = 5
height = 2

button_1 = Button(text = "1", width = width, height = height, command = lambda: button_click(1))
button_2 = Button(text = "2", width = width, height = height, command = lambda: button_click(2))
button_3 = Button(text = "3", width = width, height = height, command = lambda: button_click(3))
button_4 = Button(text = "4", width = width, height = height, command = lambda: button_click(4))
button_5 = Button(text = "5", width = width, height = height, command = lambda: button_click(5))
button_6 = Button(text = "6", width = width, height = height, command = lambda: button_click(6))
button_7 = Button(text = "7", width = width, height = height, command = lambda: button_click(7))
button_8 = Button(text = "8", width = width, height = height, command = lambda: button_click(8))
button_9 = Button(text = "9", width = width, height = height, command = lambda: button_click(9))
button_0 = Button(text = "0", width = round(width * 2.6), height = height, command = lambda: button_click(0))

button_delete = Button(text = "AC", width = width, height = height, command = lambda: delete())
button_open_parenthesis = Button(text = "(", width = width, height = height, command = lambda: button_click("("))
button_close_parenthesis = Button(text = ")", width = width, height = height, command = lambda: button_click(")"))
button_dot = Button(text = ".", width = width, height = height, command = lambda: button_click("."))

button_div = Button(text = "/", width = width, height = height, command = lambda: button_click("/"))
button_mult = Button(text = "*", width = width, height = height, command = lambda: button_click("*"))
button_sust = Button(text = "-", width = width, height = height, command = lambda: button_click("-"))
button_add = Button(text = "+", width = width, height = height, command = lambda: button_click("+"))
button_result = Button(text = "=", width = width, height = height, command = lambda: result())


# button grid position
x_pad = 2
y_pad = 2

button_delete.grid(row = 1, column = 0, padx = x_pad, pady = y_pad)
button_open_parenthesis.grid(row = 1, column = 1, padx = x_pad, pady = y_pad)
button_close_parenthesis.grid(row = 1, column = 2, padx = x_pad, pady = y_pad)
button_div.grid(row = 1, column = 3, padx = x_pad, pady = y_pad)

button_7.grid(row = 2, column = 0, padx = x_pad, pady = y_pad)
button_8.grid(row = 2, column = 1, padx = x_pad, pady = y_pad)
button_9.grid(row = 2, column = 2, padx = x_pad, pady = y_pad)
button_mult.grid(row = 2, column = 3, padx = x_pad, pady = y_pad)

button_4.grid(row = 3, column = 0, padx = x_pad, pady = y_pad)
button_5.grid(row = 3, column = 1, padx = x_pad, pady = y_pad)
button_6.grid(row = 3, column = 2, padx = x_pad, pady = y_pad)
button_sust.grid(row = 3, column = 3, padx = x_pad, pady = y_pad)

button_1.grid(row = 4, column = 0, padx = x_pad, pady = y_pad)
button_2.grid(row = 4, column = 1, padx = x_pad, pady = y_pad)
button_3.grid(row = 4, column = 2, padx = x_pad, pady = y_pad)
button_add.grid(row = 4, column = 3, padx = x_pad, pady = y_pad)

button_0.grid(row = 5, column = 0, columnspan = 2, padx = x_pad, pady = y_pad)
button_dot.grid(row = 5, column = 2, padx = x_pad, pady = y_pad)
button_result.grid(row = 5, column = 3, padx = x_pad, pady = y_pad)

window.mainloop()