class AIAgent:
    def __init__(self, id):
        self.id = id
        self.task = None

    def assign_task(self, task):
        self.task = task

    def perform_task(self):
        if self.task:
            print(f'Agent {self.id} is performing task: {self.task}')
            self.task = None