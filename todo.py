import sys

todo_list = []

def load_tasks():
    try:
        f = open("todo.txt", 'r')
        f_content = f.read().split("\n")
        f.close()
        for todo in f_content:
            if todo:
                todo_list.append(todo.split("|"))        
    except FileNotFoundError as fnfe:
        print("No Tasks Added!")

def list_tasks():
    for i, todo in enumerate(todo_list):
        print(i, todo[0], todo[1], todo[2], sep=" | ")

def save_tasks():
    f = open('todo.txt', 'w')
    for td in todo_list:
        f.write("|".join(td) + "\n")
    f.close()

def add_task(task_name, task_description):
    todo_list.append([task_name, task_description, 'pending'])
    save_tasks()
    print('New Task Added')

def update_task(task_number, status):
    todo_task = todo_list[task_number]
    todo_task[2] = status
    save_tasks()
    print(f"Task number {task_number} is updated to {status}")
    print(task_number, "|", " | ".join(todo_task))

def delete_task(task_number):
    todo_list.pop(task_number)
    save_tasks()
    print(f"Task number {task_number} is deleted")

def help():
    print("You can try any one of the following:")
    print("1. Add Task : python todo.py add '{task_name}' '{task_description}'")
    print("2. Update Task : python todo.py update '{task_number}' '{task_status}'")
    print("3. Delete Task : python todo.py delete '{task_number}'")
    print("4. List Tasks : python todo.py list'")

def main():
    load_tasks()

    args_length = len(sys.argv)

    if args_length > 1 and args_length <= 4:
        if sys.argv[1] == 'add' and args_length == 4:
            task_name, task_description = sys.argv[2], sys.argv[3]
            add_task(task_name, task_description)
        elif sys.argv[1] == 'update' and args_length == 4:
            task_number, task_status = int(sys.argv[2]), sys.argv[3]
            update_task(task_number, task_status)
        elif sys.argv[1] == 'delete' and args_length == 3:
            task_number = int(sys.argv[2])
            delete_task(task_number)
        elif sys.argv[1] == 'list' and args_length == 2:
            list_tasks()
        else:
            help()
    else:
        help()

main()
 