import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_create_task(self):
        task = {'id': 1, 'name': 'Test Task'}
        self.task_manager.create_task(task)
        self.assertEqual(self.task_manager.tasks, [task])

    def test_update_task(self):
        task = {'id': 1, 'name': 'Test Task'}
        updated_task = {'id': 1, 'name': 'Updated Task'}
        self.task_manager.create_task(task)
        self.task_manager.update_task(1, updated_task)
        self.assertEqual(self.task_manager.tasks, [updated_task])

    def test_track_tasks(self):
        task = {'id': 1, 'name': 'Test Task'}
        self.task_manager.create_task(task)
        self.assertEqual(self.task_manager.track_tasks(), [task])

if __name__ == '__main__':
    unittest.main()