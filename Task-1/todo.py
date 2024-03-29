import tkinter as tk
from tkinter import messagebox
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task():
    task_name = entry.get()
    if task_name:
        tasks.append({"name": task_name, "completed": False})
        listbox.insert(tk.END, task_name)
        entry.delete(0, tk.END)
        save_tasks(tasks)
    else:
        messagebox.showwarning("Empty Task", "Task name cannot be empty!")
        
def update_task():
    selected_index = listbox.curselection()
    if selected_index:
        task_number = selected_index[0]
        new_name = entry.get()
        if new_name:
            tasks[task_number]["name"] = new_name
            listbox.delete(task_number)
            listbox.insert(task_number, new_name)
            entry.delete(0, tk.END)
            save_tasks(tasks)
        else:
            messagebox.showwarning("Empty Task", "Task name cannot be empty!")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")


def mark_task_complete():
    selected_index = listbox.curselection()
    if selected_index:
        task_number = selected_index[0]
        tasks[task_number]["completed"] = True
        listbox.itemconfig(task_number, {"bg": "#C0C0C0"})
        save_tasks(tasks)
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")

def delete_task():
    selected_index = listbox.curselection()
    if selected_index:
        task_number = selected_index[0]
        del tasks[task_number]
        listbox.delete(task_number)
        save_tasks(tasks)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

root = tk.Tk()
root.title("To-Do List")

tasks = load_tasks()

label = tk.Label(root, text="Task:")
label.pack(padx=10)

entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=2)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(pady=2)

mark_button = tk.Button(root, text="Mark as Complete", command=mark_task_complete)
mark_button.pack(pady=2)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=2)

listbox = tk.Listbox(root, selectbackground="#00C000", activestyle="none", width=40, height=10)
listbox.pack(padx=10, pady=5)

for task in tasks:
    listbox.insert(tk.END, task["name"])
    if task["completed"]:
        listbox.itemconfig(listbox.size() - 1, {"bg": "#C0C0C0"})

root.mainloop()
