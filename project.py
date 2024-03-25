print("Welcome to the To-Do List App!")

# To-Do List features
tasks = []

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to view tasks
def view_tasks():
    if (len(tasks) == 0):
        print("No tasks to display.")
    else:
        print("List of tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

# Function to delete a task                
def delete_task():
    if (len(tasks) == 0):
        print("No tasks to display.")
    else:
        view_tasks()
        task_number = int(input("Enter the task number to delete: "))
        tasks.remove(tasks[task_number - 1])

# Function to continue the program
def continue_program():
    input_continue = input("Press enter to continue: ")
    if input_continue:
        print("Thank you for using the To-Do List App!")
        return False
    return True

# Function to mark a task as complete
def mark_task():
    if (len(tasks) == 0):
        print("No tasks to display.")
    else:
        view_tasks()
        task_number = int(input("Enter the task number to mark as complete: "))
        tasks[task_number - 1] = tasks[task_number - 1] + " (Complete)"
    
# Main loop
while True:
    try:
        # Menu
        if continue_program():
            print("Menu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Exit")
            input_choice = int(input("Enter your choice: "))
            if input_choice == 1:
                add_task()
            elif input_choice == 2:
                view_tasks()
            elif input_choice == 3:
                mark_task()
            elif input_choice == 4:
                delete_task()
            elif input_choice == 5:
                break
            else:
                print("Invalid choice. Please enter a valid choice.")
        else:
            break
    
    # Exception handling  
    except ValueError:
        print("Invalid input. Please enter a number.")
    except NameError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print("An error occurred: ", e)
    else:
        continue
    finally:
        pass
    
