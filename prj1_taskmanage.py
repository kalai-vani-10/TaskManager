tasklist = []

class task:
    def __init__(self,id,title,description,priority,status):
        self.id=id
        self.title=title
        self.description=description
        self.priority=priority
        self.status=status

    def add_task(self):
        tasklist.append(self)
        print("Task Added Succesfully")     

    def edit_task(self,title=None,description=None,priority=None,status=None):
        if title:
            self.title=title
        if description:
            self.description=description
        if priority:
            self.priority=priority
        if status:
            self.status=status
        print("Task Edited Succesfully")
        
    def delete_task(self):
        tasklist.remove(self)
        print("Task Deleted Succesfully")   
    
    @staticmethod   
    def get_task_by_id(task_id):
        for i in tasklist:
            if i.id==task_id:
                return i
        return None

    @staticmethod
    def view_all_tasks():
        for task in tasklist:
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Priority: {task.priority}, Status: {task.status}")

    @staticmethod
    def filter_tasks_by_priority(priority):
        filtered_tasks = [task for task in tasklist if task.priority.lower() == priority.lower()]
        for task in filtered_tasks:
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Priority: {task.priority}, Status: {task.status}")

def print_menu():
    print("=" * 50)
    print(" " * 16 + "Task Management" + " " * 16)
    print("=" * 50)
    print("1. Adding Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Get Task By ID")
    print("5. View All Tasks")
    print("6. Filter Tasks By Priority")
    print("7. Exit")
    print("=" * 50)

while True:
    print_menu()
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        id= input("Enter Tasks ID")
        title=input("Enter Tasks Title")
        description=input("Give Description for the task:")
        priority=input("Give Priority for that task(High / Medium / Low)")
        status=input("Enter the status of the task(Pending / In Progress / Completed)")
        tasks = task(id,title,description,priority,status)
        tasks.add_task()
        print("-" * 50)
        
    elif choice==2:
        id=input("Enter task ID to be Edit:")
        task=task.get_task_by_id(id)
        if task:
            
            title=input("Enter New Tasks Title")
            description=input("Give New Description for the task:")
            priority=input("Give New Priority for that task(High / Medium / Low)")
            status=input("Enter New status of the task(Pending / In Progress / Completed)")
            task.edit_task(title,description,priority,status)
        else:
            print("Task not found")
        print("-" * 50)

    elif choice==3:
        id=input("Enter the Id To Deleted")
        task=task.get_task_by_id(id)
        if task:
            task.delete_task()
        else:
            print("Task Not Found")

        print("-" * 50)

    elif choice==4:
        id=input("Enter the Id to get")
    
        task=task.get_task_by_id(id)
        if task:
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Priority: {task.priority}, Status: {task.status}")
        else:
            print("Task Not Found")
        print("-" * 50)
       

    elif choice==5:
        task.view_all_tasks()
        print("-" * 50)

    elif choice==6:
        priority=input("Enter Priority to filter")
        task.filter_tasks_by_priority(priority)
        print("-" * 50)
    elif choice==7:
        break

    else:
        print("Invalid")