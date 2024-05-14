def add_task(name, description, priority, time, status):
    todo = load_tasks()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'name': name,
        'description': description,
        'priority': priority,
        'time': time,
        'status': status
    }
    todo.append(task)
    print("Task added successfully.")
