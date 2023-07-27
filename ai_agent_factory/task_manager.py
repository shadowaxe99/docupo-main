class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)

    def update_task(self, task_id, task):
        self.tasks[task_id] = task

    def track_task(self, task_id):
        return self.tasks[task_id]