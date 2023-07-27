import unittest
from ai_agent import AIAgent

class TestAIAgent(unittest.TestCase):
    def setUp(self):
        self.ai_agent = AIAgent()

    def test_add_task(self):
        task = 'Test Task'
        self.ai_agent.add_task(task)
        self.assertEqual(self.ai_agent.tasks, [task])

    def test_perform_tasks(self):
        task = 'Test Task'
        self.ai_agent.add_task(task)
        self.ai_agent.perform_tasks()
        self.assertEqual(self.ai_agent.tasks, [])

if __name__ == '__main__':
    unittest.main()