from task_manager import TaskManager

task_manager = TaskManager()
task = {'id': 1, 'name': 'Test Task'}
task_manager.create_task(task)
print(task_manager.tasks)