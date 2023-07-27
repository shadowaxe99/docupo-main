from task_manager import TaskManager
from ai_agent_factory import AIAgentFactory

class TaskMaster:
    def __init__(self):
        self.task_manager = TaskManager()
        self.ai_agent_factory = AIAgentFactory()

    def assign_task(self, task):
        agent = self.ai_agent_factory.create_agent()
        agent.add_task(task)
        self.task_manager.create_task(task)

    def control_factory(self):
        for agent in self.ai_agent_factory.agents:
            for task in agent.tasks:
                agent.perform_tasks()
                self.task_manager.update_task(task['id'], task)