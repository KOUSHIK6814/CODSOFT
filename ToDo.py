import tkinter as tk

tasks = []


def add_task(task):
    tasks.append(task)
    print("Task added successfully.")


# def list_tasks():
#     if not tasks:
#         print("No tasks found.")
#     else:
#         print("Tasks:")
#         for index, task in enumerate(tasks, start=1):
#             print(f"{index}. {task}")


def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f"Completed task: {completed_task}")
    else:
        print("Invalid task index.")


window = tk.Tk()
window.title("Todo List App")
window.config(bg="#87CEEB")

# Create a listbox to display the tasks
task_listbox = tk.Listbox(window, width=50,font=("Helevtica",15), bg= "#87CEEB", fg="red")
task_listbox.pack()


def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)


# Create an entry field and buttons
task_entry = tk.Entry(window, width=20, font=("Helvetica", 20),bg = "#87CEEB", fg="red")
task_entry.pack()

frame = tk.Frame(window, bg = "#87CEEB")
frame.pack()
add_button = tk.Button(frame, text="Add Task", command=add_task, bd=0, bg = "#87CEEB", fg="black")
add_button.grid(row=0,column=0,padx=20,pady=20)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task, bd=0, bg = "#87CEEB", fg="black")
delete_button.grid(row=0,column=1,padx=20,pady=20)

# Run the Tkinter event loop
window.mainloop()
