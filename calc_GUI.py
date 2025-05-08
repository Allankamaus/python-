#setup the gui window
import tkinter as tk
from math import sqrt

def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def equalpress():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = result  # Allow further operations
    except:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")

def press_sqrt():
    try:
        global expression
        result = str(sqrt(float(expression)))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# GUI setup
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

expression = ""
input_text = tk.StringVar()

input_frame = tk.Frame(window)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 20, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Buttons
buttons_frame = tk.Frame(window)
buttons_frame.pack()

# Update button styles and add square root functionality
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('√', 5, 0)  # Add square root button
]

for (text, row, col) in buttons:
    if text == '√':
        action = press_sqrt
    else:
        action = lambda x=text: press(x) if x not in ['=', 'C'] else equalpress() if x == '=' else clear()
    tk.Button(buttons_frame, text=text, width=12, height=4, font=('Helvetica', 18, 'bold'), fg='white', bg='black', command=action).grid(row=row, column=col)

window.mainloop()
