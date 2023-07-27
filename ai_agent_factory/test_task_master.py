import unittest
from task_master import TaskMaster

class TestTaskMaster(unittest.TestCase):
    def setUp(self):
        self.task_master = TaskMaster()

    def test_assign_task(self):
        task = {'id': 1, 'name': 'Test Task'}
        self.task_master.assign_task(task)
        self.assertIn(task, self.task_master.task_manager.tasks)
        self.assertEqual(self.task_master.ai_agent_factory.agents[0].tasks, [task])

    def test_control_factory(self):
        task = {'id': 1, 'name': 'Test Task'}
        self.task_master.assign_task(task)
        self.task_master.control_factory()
        self.assertEqual(self.task_master.ai_agent_factory.agents[0].tasks, [])

if __name__ == '__main__':
    unittest.main()