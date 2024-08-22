

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def view_tasks(self):
        print("Your tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
            print(f"Task {task_number} deleted!")
        except IndexError:
            print("Invalid task number!")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        print("Tasks saved to tasks.txt!")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            print("Tasks loaded from tasks.txt!")
        except FileNotFoundError:
            print("No saved tasks found!")


def main():
    todo = ToDoList()

    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Save tasks")
        print("5. Load tasks")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to delete: "))
            todo.delete_task(task_number)
        elif choice == "4":
            todo.save_tasks()
        elif choice == "5":
            todo.load_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
