class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter a new task: ")
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("List of tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete.")
        else:
            self.view_tasks()
            try:
                choice = int(input("Enter the task number to delete: "))
                if 1 <= choice <= len(self.tasks):
                    del self.tasks[choice - 1]
                    print("Task deleted successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

    def start(self):
        while True:
            print("\n***** To-Do List *****")
            print("1. Add task")
            print("2. View tasks")
            print("3. Delete task")
            print("4. Quit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                print("Thank you for using the to-do list.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.start()
