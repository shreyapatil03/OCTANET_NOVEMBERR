# Simple To-Do List

# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed:", task)
    else:
        print("Task not found.")

# Function to display the current tasks
def display_tasks():
    if tasks:
        print("Current Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks to display.")

# Example usage
add_task("Complete homework")
add_task("Buy groceries")
display_tasks()
remove_task("Buy groceries")
display_tasks()