class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)

    def update_task(self, task_id, updated_task):
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks[i] = updated_task
                break

    def track_tasks(self):
        return self.tasks