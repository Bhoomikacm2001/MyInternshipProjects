class Task:
    def __init__(self, description):
        self.description = description

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task.description}' removed from the to-do list.")
        else:
            print("Invalid task index. Please enter a valid index.")

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task.description}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task_description = input("Enter the task description: ")
            task = Task(task_description)
            todo_list.add_task(task)
            print(f"Task '{task_description}' added to the to-do list.")
        elif choice == '3':
            todo_list.display_tasks()
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '4':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
