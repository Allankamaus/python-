import tkinter as tk
from datetime import time 

root = tk.Tk()
root.title("TO-DO List")
root.geometry("400x400")
root.resizable(True, True)

listbox = tk.Listbox(root, width=50, height=20)

class Task:
    def __init__(self,name, time, done):
        self.name = name
        self.time = time
        self.done = done
    def __str__(self):
        return f"{self.name} at {self.time.strftime('%H:%M')} - Done: {self.done}"
    def __repr__(self):
        return f"{self.name} at {self.time.strftime('%H:%M')} - Done: {self.done}"


tasks = []

#function to display tasks
def display_tasks():
    #listbox.delete(0, tk.END)
    for task in tasks:
        display_str = f"{task.name} at {task.time.strftime('%H:%M')} - Done: {task.done}"
        listbox.insert(tk.END, task)


name_entry = tk.Entry(root)
time_entry = tk.Entry(root)


#function to add tasks
def add_tasks():
    name = name_entry.get()
    time_str = time_entry.get()
    try:
        # Parse time in HH:MM format
        hour, minute = map(int, time_str.split(":"))
        t = time(hour, minute)
        task = Task(name, t, "No")
        tasks.append(task)
        listbox.insert(tk.END, str(task))
        name_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
    except Exception as e:
        listbox.insert(tk.END, "Invalid time format. Use HH:MM.")

def delete_tasks():
    try:
        selected_task_index = listbox.curselection()
        tasks.pop(selected_task_index[0])
        listbox.delete(selected_task_index)
    except Exception as e:
        listbox.insert(tk.END, "Select a task to delete.")

#Function to mark a completed task
def mark_completed():
    try:
        selected_task_index = listbox.curselection()
        task = tasks[selected_task_index[0]]
        task.done = "Yes"
        listbox.delete(selected_task_index)
    except Exception as e:
        listbox.insert(tk.END, "Select a task to mark as completed.")


label_name = tk.Label(root, text="Task Name:")
label_time = tk.Label(root, text="Time (HH:MM):")
btn = tk.Button(root, text="Add Task", command=add_tasks)
delete_btn = tk.Button(root, text = "Delete task", command = delete_tasks)
complete_btn = tk.Button(root, text = "Mark as Done", command = mark_completed)


label = tk.Label(root, text="Enter a task:")
btn = tk.Button(root, text="Add Task", command=add_tasks)



listbox.pack()
label_name.pack()
name_entry.pack()
label_time.pack()
time_entry.pack()
btn.pack()
delete_btn.pack()
complete_btn.pack()

tasks = [Task("wake up", time(6, 00),"No"), 
         Task("eat breakfast", time(7, 00),"No")]

display_tasks()

#refresh_listbox()

root.mainloop()