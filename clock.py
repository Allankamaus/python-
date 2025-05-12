import tkinter as tk
import clock
import time
import datetime

def clock():
    current_time = time.strftime('%H:%M:%S')
    label.config(text =  current_time)
    root.after(1000, clock)

root = tk.Tk()
root.title('Clock')
root.geometry('100x100')
root.resizable(False,False)
label = tk.Label()


label.pack()
clock()
root.mainloop()

